import datetime
import random


from sqlalchemy import create_engine, select, update, delete, func
from sqlalchemy.orm import Session
from models import Experiment, DataPoint


engine = create_engine("sqlite:///eksperymenty.db")


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

    session.execute(delete(DataPoint))
    session.execute(delete(Experiment))
    session.commit()