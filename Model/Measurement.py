from sqlalchemy import Column, Text, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from Model.BaseModel import BaseModel


class Measurement(BaseModel):
    __tablename__ = 'measurements'

    client_id = Column(Integer, ForeignKey('clients.id'))
    address_id = Column(Integer, ForeignKey('address.id'))
    comments = Column(Text)
    date_measure = Column(Text)
    complited = Column(Boolean)

    client = relationship('Client', foreign_keys=[client_id])
    address = relationship('Address', foreign_keys=[address_id])


