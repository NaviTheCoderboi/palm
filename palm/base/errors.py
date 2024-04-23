__all__: tuple[str, ...] = ("PipeValidationError", "SchemaValidationError")


class SchemaValidationError(Exception):
    pass


class PipeValidationError(Exception):
    pass
