from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship


from Model.BaseModel import BaseModel


class Client(BaseModel):
    __tablename__ = 'clients'

    user_id = Column(Integer, ForeignKey('users.id'))
    client_surname = Column(Text)
    client_name = Column(Text, nullable=False)
    client_firstname = Column(Text)
    client_telephone = Column(Text, nullable=False)
    client_last_telephone = Column(Text)
    client_email = Column(Text)
    client_comments = Column(Text)

    user = relationship('User', foreign_keys=[user_id])


