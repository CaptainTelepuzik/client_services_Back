from sqlalchemy import Column, Text
from sqlalchemy.orm import relationship


from Model.BaseModel import BaseModel


class Adress(BaseModel):
    __tablename__ = 'adress'

    city_name = Column(Text, nullable=False)
    street_name = Column(Text, nullable=False)
    number_build = Column(Text, nullable=False)
    number_corp = Column(Text)
    number_room = Column(Text)




