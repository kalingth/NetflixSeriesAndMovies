# from .. import db

from . import ModelBase
import sqlalchemy as sa
from datetime import datetime


class Movies(ModelBase):
    __tablename__: str = "movies"

    id: int = sa.Column(sa.INTEGER, primary_key=True, autoincrement=True)
    title: str = sa.Column(sa.String(70), nullable=False)
    lastView: datetime = sa.Column(sa.DateTime, nullable=False)

    def __repr__(self):
        # type: () -> str
        return f"<Filme: {self.title}>"

    def __init__(self, title, lastView):
        # type: (str, datetime) -> None
        self.title = title
        self.lastView = lastView
