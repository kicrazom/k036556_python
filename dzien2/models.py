import datetime


from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

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
