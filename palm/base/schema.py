from __future__ import annotations

import typing as t
from abc import ABC, abstractmethod

from palm.base.pipe import Pipe
from palm.base.validation import Result

__all__: tuple[str, ...] = ("Schema",)


class Schema(ABC):
    @abstractmethod
    def __init__(self, errorMessage: str | None = None, pipes: list[Pipe] = []) -> None:
        self.errorMessage = errorMessage
        self.pipes = pipes

    @abstractmethod
    def validate(self, data: t.Any, safeParse: bool = False) -> Result[t.Any]:
        initial = Result(data, True, [])
        for pipe in self.pipes:
            result = pipe.validate(initial, safeParse)
            initial.value = result.value
        if len(initial.issues) > 0:
            initial.success = False
        return initial
