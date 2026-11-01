import datetime


from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


eksperymenty_badani = Table(
    "eksperymenty_badani",
    Base.metadata,
    Column("eksperymenty_title", ForeignKey("eksperymenty.id"), primary_key=True),
    Column("badani_title", ForeignKey("badani.id"), primary_key=True),
)

class Experiment(Base):
    __tablename__ = "eksperymenty"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    created_at: Mapped[datetime.datetime]
    type: Mapped[int]
    finished: Mapped[bool] = mapped_column(default=False)
    punkty_title: Mapped[list["DataPoint"]] = relationship(back_populates="eksperyment_title")
    badani: Mapped[list["Subject"]] = relationship(secondary=eksperymenty_badani, back_populates="eksperymenty")

class DataPoint(Base):
    __tablename__ = "data"
    id: Mapped[int] = mapped_column(primary_key=True)
    real_value: Mapped[float]
    target_value: Mapped[float]
    eksperyment_id: Mapped[int] = mapped_column(ForeignKey("eksperymenty.id"))
    eksperyment_title: Mapped["Experiment"] = relationship(back_populates="punkty_title")


class Subject(Base):
    __tablename__ = "badani"
    id: Mapped[int] = mapped_column(primary_key=True)
    gdpr_accepted: Mapped[bool] = mapped_column(default=False)
    eksperymenty: Mapped[list["Experiment"]] = relationship(secondary=eksperymenty_badani, back_populates="badani")




