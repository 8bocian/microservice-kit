from abc import abstractmethod, ABC

class BaseLifecycleComponent(ABC):
    @abstractmethod
    async def start(self): ...
    @abstractmethod
    async def stop(self): ...