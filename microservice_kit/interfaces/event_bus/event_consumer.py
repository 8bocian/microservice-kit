from abc import ABC, abstractmethod
from typing import Awaitable, Callable
from microservice_kit.interfaces.lifecycle_component import BaseLifecycleComponent
from microservice_kit.interfaces.event_bus.models import Event

class BaseEventConsumer(BaseLifecycleComponent, ABC):
    @abstractmethod
    def register_handler(self, queue: str, handler: Callable[[Event], Awaitable[None]]) -> None:
        ...

    def subscribe(self, queue: str):
        def decorator(handler: Callable[[Event], Awaitable[None]]):
            self.register_handler(queue, handler)
            return handler
        return decorator
