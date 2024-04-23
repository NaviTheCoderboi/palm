from palm.base.errors import PipeValidationError
from palm.base.pipe import Pipe
from palm.base.validation import Issue, Result
from palm.schemas import String


class MinLength(Pipe[str]):
    def __init__(self, length: int, errorMessage: str | None = None) -> None:
        self.length = length
        super().__init__(errorMessage)

    def validate(self, data: Result[str], safeParse: bool) -> Result[str]:
        if len(data.value) < self.length:
            issue = Issue(
                input=str(data.value),
                expected=f">{self.length}",
                description=(
                    f"The input data is shorter than {self.length} characters."
                    if self.errorMessage is None
                    else self.errorMessage
                ),
            )
            data.issues.append(issue)
            if not safeParse:
                raise PipeValidationError(issue.format() + "\n---")
            return data
        return data


t = String([MinLength(2)])


print(t.validate(232323, True))
print(t.validate("1", True))
