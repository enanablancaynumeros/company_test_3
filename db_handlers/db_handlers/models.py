from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime, BigInteger
from sqlalchemy_utils.types.choice import ChoiceType

from db_handlers.postgres_config import Base

gender_choices = [
    ("Man", "Man"),
    ("Woman", "Woman"),
]


class Client(Base):
    __tablename__ = 'client'

    id = Column(BigInteger, primary_key=True)
    visits = relationship("Visits", back_populates="client", order_by="desc(Action.timestamp)", lazy='joined')

    def _to_dict(self):
        return dict(
            id=self.id,
        )


class Visits(Base):
    __tablename__ = 'visits'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    client_id = Column(BigInteger, ForeignKey('client.id'))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    gender = Column(ChoiceType(gender_choices), nullable=False)

    def _to_dict(self):
        return dict(
            id=self.id,
            gender=self.gender.value,
            client=self.client_id
        )
