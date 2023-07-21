from classes.BaseClass import BaseClass
from Model.Measurement import Measurement as MeasurementModel



class Measurement(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False) -> MeasurementModel:
        return MeasurementModel() if new_model else MeasurementModel

    def _prepare_query_filter(self, query, filter_params):

        if filter_params.get('selectedDay'):
            value = filter_params.get('selectedDay')
            query = query.where(self.get_model().date_measure == value)
            return query























