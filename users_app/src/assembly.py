from adapters.memory.user_repository_adapter import InMemoryUserRepositoryAdapter
from adapters.postgres.user_repository_adapter import PostgresUserRepositoryAdapter
from domain.use_cases.authenticate_user_use_case import AuthenticateUserUseCase
from domain.use_cases.base_use_case import BaseUseCase
from domain.use_cases.count_users_use_case import CountUsersUseCase
from domain.use_cases.create_user_use_case import CreateUserUseCase
from domain.use_cases.delete_user_use_case import DeleteUserUseCase
from domain.use_cases.get_current_user_use_case import GetCurrentUserUseCase
from domain.use_cases.get_user_use_case import GetUserUseCase
from domain.use_cases.get_users_use_case import GetAllUsersUseCase
from domain.use_cases.reset_users_use_case import ResetUsersUseCase
from domain.use_cases.update_user_use_case import UpdateUserUseCase
from config.database import SessionLocal

# Instancia única global
user_repository = InMemoryUserRepositoryAdapter()
auth_use_case = AuthenticateUserUseCase(user_repository)

db_session = SessionLocal()
repository = PostgresUserRepositoryAdapter(db_session)


def build_create_user_use_case() -> BaseUseCase:
    """Get create user use case."""
    return CreateUserUseCase(user_repository)


def build_get_user_use_case() -> BaseUseCase:
    """Get user use case."""
    return GetUserUseCase(user_repository)


def build_get_users_use_case() -> BaseUseCase:
    """Get users use case."""
    return GetAllUsersUseCase(user_repository)


def build_update_user_use_case() -> BaseUseCase:
    """Update user use case."""
    return UpdateUserUseCase(user_repository)


def build_delete_user_use_case() -> BaseUseCase:
    """Get delete user use case."""
    return DeleteUserUseCase(user_repository)


def build_authenticate_user_use_case() -> AuthenticateUserUseCase:
    """Get authenticate user use case."""
    return auth_use_case  # devuelve la misma instancia


def build_count_users_use_case() -> CountUsersUseCase:
    """Get count users use case."""
    return CountUsersUseCase(user_repository)


def build_get_current_user_use_case() -> GetCurrentUserUseCase:
    return GetCurrentUserUseCase(auth_use_case)


def build_reset_users_use_case() -> ResetUsersUseCase:
    return ResetUsersUseCase(user_repository)
