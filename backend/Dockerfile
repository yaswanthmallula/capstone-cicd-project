FROM python:3.11-slim

WORKDIR /app

# Install dependencies globally
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd appuser
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
