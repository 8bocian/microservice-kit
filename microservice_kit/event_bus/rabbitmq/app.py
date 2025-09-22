from typing import Callable, Awaitable
from microservice_kit.interfaces.event_consumer import BaseEventConsumer
from microservice_kit.interfaces.event_publisher import BaseEventPublisher
from microservice_kit.interfaces.event_bus import BaseEventBus


class RabbitMQ(BaseEventBus):
    def __init__(self, publisher: BaseEventPublisher, consumer: BaseEventConsumer):
        self.publisher = publisher
        self.consumer = consumer

    async def publish(self, topic: str, event: dict) -> None:
        await self.publisher.publish(topic, event)

    def subscribe(self, topic: str, handler: Callable[[dict], Awaitable[None]] | None = None) -> Callable[
        [Callable[[dict], Awaitable[None]]], Callable[[dict], Awaitable[None]]]:

    async def start(self):
        await self.publisher.start()
        await self.consumer.start()

    async def stop(self):
        await self.publisher.stop()
        await self.consumer.stop()
