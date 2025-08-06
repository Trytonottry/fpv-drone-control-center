FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src/
EXPOSE 5000

ENV PYTHONPATH=/app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "src.web.app:app"]