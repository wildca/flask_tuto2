from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from app import Base


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)

    user = relationship('User', back_populates="address")

    def __init__(self, city='Jicin'): # default value
        self.city = city
