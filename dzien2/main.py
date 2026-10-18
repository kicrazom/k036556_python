import datetime
import sqlalchemy


from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class Experiment(Base):
    __tablename__ = "experiments"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    created_at: Mapped[datetime.datetime]
    type: Mapped[int]
    finished: Mapped[bool] = mapped_column(default=False)

class DataPoint(Base):
    __tablename__ = "data"
    id: Mapped[int] = mapped_column(primary_key=True)
    real_value: Mapped[float]
    target_value: Mapped[float]


engine = create_engine("sqlite:///eksperymenty.db")

Base.metadata.create_all(engine)
