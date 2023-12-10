from contextlib import contextmanager
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker, Session


SESSION: scoped_session | None = None
ENGINE: Engine | None = None

Base = declarative_base()


def initialize_database(db_uri: str) -> None:
    global SESSION, ENGINE
    ENGINE = create_engine(db_uri, pool_pre_ping=True)
    session_factory = sessionmaker(ENGINE)
    SESSION = scoped_session(session_factory)


@contextmanager
def get_session() -> Generator[Session, None, None]:
    try:
        yield SESSION
    except Exception:
        SESSION.rollback()
        raise


def create_all_tables() -> None:
    """Create all tables in status db."""
    with get_session() as session:
        Base.metadata.create_all(bind=session.get_bind())


def setup_test_database() -> None:
    initialize_database("sqlite:///:memory:")
    create_all_tables()
