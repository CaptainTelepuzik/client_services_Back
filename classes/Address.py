from classes.BaseClass import BaseClass
from Model.Address import Address as AddressModel


class Address(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False) -> AddressModel:
        return AddressModel() if new_model else AddressModel

    def _prepare_query_filter(self, query, filter_params):

        if filter_params.get('searchAddress'):
            value = filter_params.get('searchAddress')
            query = query.where(self.get_model().street_name == value)
            return query

        else:
            return



