from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def hello():
    return {
        "ok": True,
        "message": "Hello v2",
        "env": os.getenv("APP_ENV", "unknown")
    }

@app.get("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)