from typing import Callable, Awaitable
from microservice_kit.interfaces.event_bus.event_consumer import BaseEventConsumer
from microservice_kit.interfaces.event_bus.event_publisher import BaseEventPublisher
from microservice_kit.interfaces.event_bus import BaseEventBus
from microservice_kit.interfaces.types import Event


class RabbitMQ(BaseEventBus):
    def __init__(self, publisher: BaseEventPublisher, consumer: BaseEventConsumer):
        self.publisher = publisher
        self.consumer = consumer

    async def publish(self, topic: str, message: Message) -> None:
        await self.publisher.publish(topic, message)

    def subscribe(self, topic: str, handler: Callable[[Event], Awaitable[None]] | None = None) -> Callable[
        [Callable[[Event], Awaitable[None]]], Callable[[Event], Awaitable[None]]]:
        ...

    async def start(self):
        await self.publisher.start()
        await self.consumer.start()

    async def stop(self):
        await self.publisher.stop()
        await self.consumer.stop()
