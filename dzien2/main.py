import datetime
import random

from sqlalchemy import create_engine, select, update, delete, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship


class Base(DeclarativeBase):
    pass

class Experiment(Base):
    __tablename__ = "eksperymenty"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    created_at: Mapped[datetime.datetime]
    type: Mapped[int]
    finished: Mapped[bool] = mapped_column(default=False)
    punkty_title: Mapped[list["DataPoint"]] = relationship(back_populates="eksperyment_title")

class DataPoint(Base):
    __tablename__ = "data"
    id: Mapped[int] = mapped_column(primary_key=True)
    real_value: Mapped[float]
    target_value: Mapped[float]
    eksperyment_id: Mapped[int] = mapped_column(ForeignKey("eksperymenty.id"))
    eksperyment_title: Mapped["Experiment"] = relationship(back_populates="punkty_title")


engine = create_engine("sqlite:///eksperymenty.db")

Base.metadata.create_all(engine)

with Session(engine) as session:
    e1 = Experiment(title= "Eksperyment nr 1", created_at=datetime.datetime.now(), type=1)
    session.add(e1)
    e2 = Experiment(title= " Eksperyment nr 2 ", created_at=datetime.datetime.now(), type=2)
    session.add(e2)

    for i in range(10):
        dp = DataPoint(real_value=random.random(), target_value=random.random())
        e1.punkty_title.append(dp)

    for i in range (10):
        dp = DataPoint(real_value=random.random(), target_value=random.random())
        e2.punkty_title.append(dp)

    for eksperyment in session.scalars(select(Experiment)):
        print(eksperyment.id, eksperyment.title, eksperyment.finished)

    for punkt_kontrolny in session.scalars(select(DataPoint)):
        print(punkt_kontrolny.id, punkt_kontrolny.real_value, punkt_kontrolny.target_value)

    session.execute(update(Experiment).values(finished=True))
    session.commit()

    for eksperyment in session.scalars(select(Experiment)):
        print("po zmianie:", eksperyment.id, eksperyment.title, eksperyment.finished)

    wynik_agregacji = (
        select(Experiment.title, func.sum(DataPoint.real_value), func.avg(DataPoint.real_value))
        .join(Experiment.punkty_title)
        .group_by(Experiment.id)
    )

    for title, suma, srednia in session.execute(wynik_agregacji):
        print(title, suma, srednia)

session.execute(delete(Experiment))
session.execute(delete(DataPoint))
session.commit()