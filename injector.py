import inject

from lab4.ExperimentConstants import ExperimentConstants
from lab4.model.ExperimentModel import ExperimentModel


class Injector:
    em = None
    ec = None

    @staticmethod
    def setParams(em, ec):
        Injector.em = em
        Injector.ec = ec
        return Injector

    @staticmethod
    def my_config(binder):
        binder.bind(ExperimentModel, Injector.em)
        binder.bind(ExperimentConstants, Injector.ec)

    @staticmethod
    def configure():
        inject.configure(Injector.my_config)
