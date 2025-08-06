FROM python:3.11-slim
WORKDIR /app
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ /app/src/
ENV PYTHONPATH=/app
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "src.web.app:app"]