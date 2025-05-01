import json
import uuid
import aio_pika
import aioredis
from .config import RABBITMQ_URL, REDIS_URL, QUEUE_NAME

async def send_scrape_task(cnpj: str):
    task_id = str(uuid.uuid4())
    redis = await aioredis.from_url(REDIS_URL)
    await redis.hset(f"task:{task_id}", mapping={"status": "pending"})

    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    channel = await connection.channel()
    await channel.default_exchange.publish(
        aio_pika.Message(body=json.dumps({"task_id": task_id, "cnpj": cnpj}).encode()),
        routing_key=QUEUE_NAME
    )
    await connection.close()
    return task_id

async def get_task_status(task_id: str):
    redis = await aioredis.from_url(REDIS_URL)
    result = await redis.hgetall(f"task:{task_id}")
    if not result:
        return None
    return {k.decode(): v.decode() for k, v in result.items()}