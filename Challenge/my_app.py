from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = int(os.environ.get("REDIS_PORT", 6379))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)


@app.route("/")
def hello_world():
    return "<p>Welcome to the Flask and Redis app!</p>"


@app.route("/count")
def count():
    visits = r.incr("visits")
    return f"<p>Visit count: {visits}</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)