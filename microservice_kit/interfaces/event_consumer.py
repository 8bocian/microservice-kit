from abc import ABC, abstractmethod
from typing import Awaitable, Callable
from microservice_kit.interfaces.lifecycle_component import BaseLifecycleComponent
from .types import Event

class BaseEventConsumer(BaseLifecycleComponent, ABC):
    @abstractmethod
    def subscribe(
            self,
            queue: str,
    ) -> Callable[[Callable[[Event], Awaitable[None]]], Callable[[Event], Awaitable[None]]]:
        """
        Can be used as a decorator:

        @consumer.subscribe("order.created")
        async def handle_order_created(event: dict) -> None:
            ...
        """
        ...
