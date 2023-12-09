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


def get_session() -> Session:
    return SESSION
