from sqlalchemy import Column, Text

from Model.BaseModel import BaseModel


class NameStreet(BaseModel):
    __tablename__ = 'namestreet'

    name_street = Column(Text)



