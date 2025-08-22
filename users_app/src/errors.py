class UserNotFoundError(Exception):
    """Exception raised when a user is not found."""

    pass

class UserAlreadyExistsError(Exception):
    """Raised when a user with the same username or email already exists."""
    pass
