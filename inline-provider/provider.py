import os

from schema import Event
import redis

QUEUE_NAME = 'line-provider-events'


def share_event(event: Event):
    connection = redis.Redis(host=os.environ['REDIS_HOST'], port=6379, db=0)
    connection.rpush(QUEUE_NAME, event.model_dump_json())
