from adapters.memory.user_repository_adapter import InMemoryUserRepositoryAdapter
from domain.use_cases.base_use_case import BaseUseCase
from domain.use_cases.create_user_use_case import CreateUserUseCase
from domain.use_cases.delete_user_use_case import DeleteUserUseCase
from domain.use_cases.get_user_use_case import GetUserUseCase
from domain.use_cases.get_users_use_case import GetAllUsersUseCase
from domain.use_cases.update_user_use_case import UpdateUserUseCase

repository: InMemoryUserRepositoryAdapter = InMemoryUserRepositoryAdapter()


def build_create_user_use_case() -> BaseUseCase:
    """Get create user use case."""
    return CreateUserUseCase(repository)


def build_get_user_use_case() -> BaseUseCase:
    """Get user use case."""
    return GetUserUseCase(repository)


def build_get_users_use_case() -> BaseUseCase:
    """Get users use case."""
    return GetAllUsersUseCase(repository)


def build_update_user_use_case() -> BaseUseCase:
    """Update user use case."""
    return UpdateUserUseCase(repository)


def build_delete_user_use_case() -> BaseUseCase:
    """Get delete user use case."""
    return DeleteUserUseCase(repository)
