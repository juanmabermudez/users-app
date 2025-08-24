from config.database import SessionLocal
from src.adapters.postgres import PostgresUserRepositoryAdapter

db_session = SessionLocal()
repository = PostgresUserRepositoryAdapter(db_session)