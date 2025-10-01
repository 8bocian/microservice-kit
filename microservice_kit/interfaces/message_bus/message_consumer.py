from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Awaitable, Callable
from microservice_kit.interfaces.lifecycle_component import BaseLifecycleComponent
from microservice_kit.interfaces.message_bus.models.message import Message
from microservice_kit.interfaces.message_bus.models.subscription import Subscription

HandlerType = Callable[[Message], Awaitable[None]]

class BaseMessageConsumer(BaseLifecycleComponent, ABC):
    @abstractmethod
    def register_handler(self, config: Subscription | None, handler: HandlerType) -> None:
        ...

    def subscribe(self, config: Subscription | None) -> Callable[[HandlerType], HandlerType]:
        """Register handler for events via a decorator

        :param config: configuration indicating where and what for the consumer should listen
        :return:
        """
        def decorator(handler: HandlerType) -> HandlerType:
            self.register_handler(config, handler)
            return handler
        return decorator
