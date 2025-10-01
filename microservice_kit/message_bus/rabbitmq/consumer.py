from __future__ import annotations
from typing import Callable, Awaitable, Dict

from aio_pika import connect_robust
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel

from microservice_kit.interfaces.message_bus.message_consumer import BaseMessageConsumer, HandlerType
from microservice_kit.interfaces.message_bus.models.subscription import Subscription


class RabbitMQConsumer(BaseMessageConsumer):
    def __init__(self, ):
        self._rabbitmq_url = None
        self.con_connection: AbstractRobustConnection | None = None
        self.con_channels: Dict[str, AbstractRobustChannel] = {}
        self.con_handlers: Dict[str, Callable] = {}

    def register_handler(self, config: Subscription | None, handler: HandlerType) -> None:
        pass

    async def start(self):
        self.con_connection = await connect_robust(self._rabbitmq_url)
        for queue_name, handler in self.con_handlers.items():
            channel = self.con_connection.channel()
            self.con_channels[queue_name] = channel

    async def stop(self):
        pass
