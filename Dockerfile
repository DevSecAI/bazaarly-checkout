# BAZ-IAC-004: runs as root.
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY bazaarly/ ./bazaarly/
EXPOSE 8000
CMD ["python", "-m", "bazaarly.wsgi"]
