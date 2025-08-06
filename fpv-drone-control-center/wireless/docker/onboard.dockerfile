FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    git screen mavproxy && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ /app/src/
ENV PYTHONPATH=/app
# mavproxy переводит MSP → MAVLink UDP:14550
CMD mavproxy.py --master=/dev/ttyUSB0 --cmd="set heartbeat 0" --out=udp:0.0.0.0:14550 \
 & python src/radio/telemetry_server.py