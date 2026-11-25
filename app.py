import os
import redis
from flask import Flask, jsonify, request

app = Flask(__name__)

GREETING = os.getenv("APP_GREETING", "Hello")

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    password=os.getenv("REDIS_PASSWORD") or None,
    decode_responses=True,
    socket_connect_timeout=2,
    socket_timeout=2
)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/ready")
def ready():
    try:
        redis_client.ping()
        return jsonify(status="ready")
    except redis.RedisError:
        return jsonify(status="not ready"), 503


@app.get("/greet")
def greet():
    name = request.args.get("name", "world")
    return jsonify(message=f"{GREETING}, {name}!")


@app.get("/visit")
def visit():
    try:
        current = redis_client.incr("visits")
        return jsonify(visits=current)
    except redis.RedisError:
        return jsonify(error="Redis connection failed"), 503


@app.get("/redis-visit")
def redis_visit():
    try:
        visits = redis_client.incr("visits")
        return jsonify(visits=visits, storage="redis")
    except redis.RedisError:
        return jsonify(error="Redis connection failed"), 503


@app.get("/info")
def info():
    return jsonify(
        application="CENG413 HW-3",
        greeting=GREETING,
        storage="redis"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)