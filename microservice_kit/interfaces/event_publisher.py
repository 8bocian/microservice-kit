from abc import ABC, abstractmethod

class BaseEventPublisher(ABC):
    @abstractmethod
    async def publish(self, topic: str, event: dict) -> None:...