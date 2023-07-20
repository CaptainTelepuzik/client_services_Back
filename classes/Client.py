from classes.BaseClass import BaseClass
from Model.Client import Client as ClientModel



class Client(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False) -> ClientModel:
        return ClientModel() if new_model else ClientModel


    def _prepare_query_filter(self, query, filter_params):

        if filter_params.get('searchTelephone'):
            value = filter_params.get('searchTelephone')
            query = query.where(self.get_model().client_telephone == value)

        if filter_params.get('id'):
            value = filter_params.get('id')
            query = query.where(self.get_model().id == value)

        if filter_params.get('onlyComplete'):
            query = query.where(self.get_model().id == None)

        return query























