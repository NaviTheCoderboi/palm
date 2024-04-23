import typing as t

from palm.base.pipe import Pipe
from palm.base.schema import Schema
from palm.base.validation import Issue, Result
from palm.utils.common import basicValidation, raiseErrorIfMessage

type T = str

__all__: tuple[str, ...] = ("String",)


class String(Schema):

    def __init__(
        self,
        pipes: list[Pipe[T]] = [],
        errorMessage: str | None = None,
    ) -> None:
        super().__init__(errorMessage, pipes)

    def validate(self, data: t.Any, safeParse: bool = False) -> Result[T]:
        if not isinstance(data, str):
            if safeParse:
                return Result(
                    data,
                    False,
                    [
                        Issue(
                            input=str(data),
                            expected="str",
                            description=(
                                "The input data is not a string."
                                if self.errorMessage is None
                                else self.errorMessage
                            ),
                        )
                    ],
                )
            else:
                raiseErrorIfMessage(
                    self.errorMessage, "schema", "The input data is not a string."
                )
        initial = Result(data, True, [])
        basicValidation(initial, self.pipes, safeParse)
        return initial
