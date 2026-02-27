class AppError(Exception):
    """Base exception for predictable app errors."""


class StageLockedError(AppError):
    """Raised when a user tries to start a locked stage."""


class NavigationError(AppError):
    """Raised when navigation cannot proceed."""