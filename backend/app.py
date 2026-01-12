import os
from flask import Flask, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

@app.route("/")
def home():
    return "Backend service with DB is running"

@app.route("/health")
def health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return jsonify(status="UP", database="CONNECTED"), 200
    except Exception as e:
        return jsonify(status="DOWN", database="ERROR", error=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
