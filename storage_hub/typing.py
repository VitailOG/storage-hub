from typing import Protocol, runtime_checkable


@runtime_checkable
class IStorage(Protocol):

    def upload(self) -> None:
        pass

    def download(self) -> bytes:
        pass

    def exists(self) -> bool:
        pass
