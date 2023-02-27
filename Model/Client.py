from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship


from Model.BaseModel import BaseModel


class Client(BaseModel):
    __tablename__ = 'tasks'

    user_id = Column(Integer, ForeignKey('users.id'))
    surname = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    firstname = Column(Text, nullable=False)
    telephone = Column(Text, nullable=False, unique=True)
    last_telephone = Column(Text, nullable=False, unique=True)

    user = relationship('User', foreign_keys=[user_id])


