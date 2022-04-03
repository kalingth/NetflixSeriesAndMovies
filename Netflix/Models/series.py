# from .. import db
from . import ModelBase
import sqlalchemy as sa
from datetime import datetime


class Series(ModelBase):
    __tablename__: str = "series"

    id: int = sa.Column(sa.INTEGER, primary_key=True, autoincrement=True)
    title: str = sa.Column(sa.String(70), nullable=False)
    season: str = sa.Column(sa.String(35))
    ep_title: str = sa.Column(sa.String(100))
    lastView: datetime = sa.Column(sa.DateTime, nullable=False)

    def __repr__(self):
        # type: () -> str
        return f"<Serie: {self.title}>"

    def __init__(self, title, season, ep_title, lastView):
        # type: (str, str, str, datetime) -> None
        self.title = title
        self.season = season
        self.ep_title = ep_title
        self.lastView = lastView
