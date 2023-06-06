from classes.BaseClass import BaseClass
from Model.Measurement import Measurement as MeasurementModel



class Measurement(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False) -> MeasurementModel:
        return MeasurementModel() if new_model else MeasurementModel

























