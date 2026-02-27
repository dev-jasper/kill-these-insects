# src/kti/domain/result.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class AppResult(Generic[T]):
    """
    Result type:
      - ok=True  => value is valid
      - ok=False => error is valid
    """
    ok: bool
    value: T | None = None
    error: Exception | None = None

    @classmethod
    def success(cls, value: T) -> AppResult[T]:
        return cls(ok=True, value=value)

    @classmethod
    def failure(cls, error: Exception) -> AppResult[T]:
        return cls(ok=False, error=error)