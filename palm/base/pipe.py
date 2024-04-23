import typing as t
from abc import ABC, abstractmethod

import typing_extensions as tx

from palm.base.validation import Result

__all__: tuple[str, ...] = ("Pipe",)

T = tx.TypeVar("T", default=t.Any)


class Pipe(ABC, tx.Generic[T]):
    @abstractmethod
    def __init__(self, errorMessage: str | None = None) -> None:
        self.errorMessage = errorMessage

    @abstractmethod
    def validate(self, data: Result[t.Any], safeParse: bool) -> Result[T]: ...
