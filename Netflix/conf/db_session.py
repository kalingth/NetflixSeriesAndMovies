import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.future.engine import Engine
from sqlalchemy_utils import database_exists, create_database

from typing import Optional, Any

from ..Models import ModelBase

ENGINE: Engine


def engineConfiguration(dbms="sqlite", user=None, password=None,
                        path="databases/SQLite/NetflixData.sqlite"):
    # type: (str, str, Optional[str], Optional[str]) -> dict

    dbmsEnginesConfigs = {
        "sqlite": {
            "url": f"sqlite:///{path}",
            "echo": False,
            "connect_args": {
                "check_same_thread": False
            }
        },
        "postgresql": {
            "url": f"postgresql://{user}:{password}@localhost:5432/{path}",
            "echo": False
        },
        "mysql": {
            "url": f"mysql://{user}:{password}@localhost:3306/{path}",
            "echo": False
        }
    }

    return dbmsEnginesConfigs[dbms]


def createEngine(*args, **kwargs):
    # type: (Any, Any) -> Optional[Engine]
    global ENGINE

    configuration = engineConfiguration(*args, **kwargs)

    ENGINE = sa.create_engine(**configuration)
    if not database_exists(ENGINE.url):
        create_database(ENGINE.url)

    return ENGINE


def createSession(*args, **kwargs):
    # type: (Any, Any) -> Session
    global ENGINE

    createEngine(*args, **kwargs)

    _session = sessionmaker(ENGINE, expire_on_commit=False, class_=Session)
    session = _session()

    return session


def createTables(*args, **kwargs):
    # type: (Any, Any) -> None
    global ENGINE

    from Netflix.Models import __databases

    createEngine(*args, **kwargs)

    print(f"\nEscopo de Execução {ENGINE.name.title()}")
    print("Criando, caso não existam: ", ", ".join(__databases.tableNames))

    ModelBase.metadata.create_all(ENGINE)
