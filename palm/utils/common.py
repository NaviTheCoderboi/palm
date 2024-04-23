import typing as t

from palm.base.errors import PipeValidationError, SchemaValidationError
from palm.base.pipe import Pipe
from palm.base.validation import Result

__all__: tuple[str, ...] = ("raiseErrorIfMessage",)


def raiseErrorIfMessage(
    message: str | None, type: t.Literal["schema", "pipe"], default: str
) -> t.NoReturn:
    if type == "pipe":
        if message is not None:
            raise PipeValidationError(message)
        else:
            raise PipeValidationError(default)
    elif type == "schema":
        if message is not None:
            raise SchemaValidationError(message)
        else:
            raise SchemaValidationError(default)
    else:
        raise ValueError("Invalid type")


def basicValidation[T](initial: Result[T], pipes: list[Pipe[T]], safeParse: bool):
    for pipe in pipes:
        result = pipe.validate(initial, safeParse)
        initial.value = result.value
    if len(initial.issues) > 0:
        initial.success = False
