from classes.BaseClass import BaseClass
from Model.Adress import Adress as AdressModel


class Adress(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False) -> AdressModel:
        return AdressModel() if new_model else AdressModel

    def _prepare_query_filter(self, query, filter_params):

        if filter_params.get('searchAdress'):
            value = filter_params.get('searchAdress')
            query = query.where(self.get_model().client_telephone == value)
            return query

        else:
            return


