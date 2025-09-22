from typing import List
from pydantic import BaseModel, validator, model_validator

from microservice_kit.interfaces.config import BaseEventBusConfig


class RabbitMQExchange(BaseModel):
    ...

class RabbitMQQueue(BaseModel):
    ...

class RabbitMQPublisherConfig(BaseModel):
    ...

class RabbitMQConsumerConfig(BaseModel):
    exchanges: List[RabbitMQExchange] = []
    queues: List[RabbitMQQueue] = []


class RabbitMQConfig(BaseEventBusConfig):
    publisher: RabbitMQPublisherConfig | None = None
    consumer: RabbitMQConsumerConfig | None = None

    @model_validator(mode="after")
    def check_at_least_one(cls, values):
        if not values.publisher and not values.consumer:
            raise ValueError("RabbitMQConfig must define at least one of publisher or consumer")
        return values