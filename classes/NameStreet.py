from classes.BaseClass import BaseClass
from Model.NameStreet import NameStreet as NameStreetModel


class NameStreet(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False) -> NameStreetModel:
        return NameStreetModel() if new_model else NameStreetModel




