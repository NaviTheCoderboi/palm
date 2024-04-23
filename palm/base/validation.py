from dataclasses import dataclass

__all__: tuple[str, ...] = ("Result",)


@dataclass()
class Issue:
    input: str
    expected: str
    description: str

    def format(self) -> str:
        return f"Input: {self.input}\nExpected: {self.expected}\nDescription: {self.description}"


@dataclass()
class Result[T]:
    value: T
    success: bool
    issues: list[Issue]
