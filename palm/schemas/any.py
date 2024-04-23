import typing as t

from palm.base.pipe import Pipe
from palm.base.schema import Schema
from palm.base.validation import Result

__all__: tuple[str, ...] = ("Any",)


class Any(Schema):
    def __init__(
        self, errorMessage: str | None = None, pipes: list[Pipe[t.Any]] = []
    ) -> None:
        super().__init__(errorMessage, pipes)

    def validate(self, data: t.Any, safeParse: bool = False) -> Result[t.Any]:
        return super().validate(data, safeParse)
