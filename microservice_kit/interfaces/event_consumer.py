from abc import ABC, abstractmethod
from typing import Awaitable, Callable


class BaseEventConsumer(ABC):
    @abstractmethod
    def subscribe(self, topic: str, handler: Callable[[dict], Awaitable[None]]) -> None:...