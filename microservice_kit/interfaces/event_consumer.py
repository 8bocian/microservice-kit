from abc import ABC, abstractmethod
from typing import Awaitable, Callable

from microservice_kit.interfaces.lifecycle_component import BaseLifecycleComponent


class BaseEventConsumer(BaseLifecycleComponent, ABC):
    @abstractmethod
    def subscribe(
            self,
            topic: str,
            handler: Callable[[dict], Awaitable[None]] | None = None
    ) -> Callable[[Callable[[dict], Awaitable[None]]], Callable[[dict], Awaitable[None]]]:
        """
        Can be used as a decorator:

        @consumer.subscribe("order.created")
        async def handle_order_created(event: dict) -> None:
            ...
        """
        ...
