from sqlalchemy import Column, Text


from Model.BaseModel import BaseModel


class Address(BaseModel):
    __tablename__ = 'address'

    city_name = Column(Text, nullable=False)
    street_name = Column(Text, nullable=False)
    number_build = Column(Text, nullable=False)
    number_corp = Column(Text)
    number_room = Column(Text)




