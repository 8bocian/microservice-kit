from typing import Callable, Awaitable, Dict

from aio_pika import connect_robust
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel

from microservice_kit.interfaces.event_bus.event_consumer import BaseEventConsumer


class RabbitMQConsumer(BaseEventConsumer):
    def __init__(self):
        self._rabbitmq_url = None
        self.con_connection: AbstractRobustConnection | None = None
        self.con_channels: Dict[str, AbstractRobustChannel] = {}
        self.con_handlers: Dict[str, Callable] = {}

    async def start(self):
        self.con_connection = await connect_robust(self._rabbitmq_url)
        for queue_name, handler in self.con_handlers.items():
            channel = self.con_connection.channel()
            self.con_channels[queue_name] = channel

    async def stop(self):
        pass

    def subscribe(self, queue_name: str):
        def decorator(func: Callable):
            self.con_handlers[queue_name] = func
            return func

        return decorator

    def subscribe(self, queue_name: str, handler: Callable[[dict], Awaitable[None]]) -> None:
        pass