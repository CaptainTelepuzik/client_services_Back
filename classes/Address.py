from classes.BaseClass import BaseClass
from Model.Address import Address as AddressModel


class Address(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False) -> AddressModel:
        return AddressModel() if new_model else AddressModel




