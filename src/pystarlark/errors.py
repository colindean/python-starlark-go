from typing import Any

__all__ = ["StarlarkError", "SyntaxError", "EvalError"]


class StarlarkError(Exception):
    def __init__(self, error: str, error_type: str, *extra_args: Any):
        super().__init__(error, error_type, *extra_args)
        self.error = error
        self.error_type = error_type

    def __str__(self) -> str:
        return self.error


class SyntaxError(StarlarkError):
    def __init__(
        self,
        error: str,
        error_type: str,
        msg: str,
        filename: str,
        line: int,
        column: int,
    ):
        super().__init__(error, error_type, msg, filename, line, column)
        self.msg = msg
        self.filename = filename
        self.line = line
        self.column = column


class EvalError(StarlarkError):
    def __init__(self, error: str, error_type: str, backtrace: str):
        super().__init__(error, error_type, backtrace)
        self.backtrace = backtrace
