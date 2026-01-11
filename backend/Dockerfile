FROM python:3.11-slim

WORKDIR /app

# 👇 IMPORTANT LINE (this fixes your issue)
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
