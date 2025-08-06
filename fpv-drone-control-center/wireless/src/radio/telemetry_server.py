import asyncio, json, time
from pymavlink import mavutil
import websockets

UDP_PORT = 14550
WS_PORT  = 8765

conn = mavutil.mavlink_connection(f'udp:0.0.0.0:{UDP_PORT}', source_system=1)
clients = set()

async def register(ws):
    clients.add(ws)

async def unregister(ws):
    clients.remove(ws)

async def tx_telemetry():
    while True:
        msg = conn.recv_match(type='ATTITUDE', blocking=True)
        if msg:
            data = {"roll": msg.roll, "pitch": msg.pitch, "yaw": msg.yaw}
            if clients:
                await asyncio.gather(*(ws.send(json.dumps(data)) for ws in clients))
        await asyncio.sleep(0.05)

async def rx_rc(websocket, path):
    await register(websocket)
    try:
        async for msg in websocket:
            rc = json.loads(msg)
            conn.mav.rc_channels_override_send(
                conn.target_system, conn.target_component,
                *rc['channels'])
    finally:
        await unregister(websocket)

async def main():
    await asyncio.gather(
        tx_telemetry(),
        websockets.serve(rx_rc, "0.0.0.0", WS_PORT)
    )
    await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())