import inject

from lab5.Experiment.Experiment import ExperimentConstants
from lab5.Kalman.Kalman import Kalman
from lab5.Experiment.Experiment import ExperimentModel


class Injector:
    em = None
    ec = None

    @staticmethod
    def setParams(em, ec):
        Injector.em = em
        Injector.ec = ec
        return Injector

    @staticmethod
    def configure():
        inject.configure(Injector.getConfig)

    @staticmethod
    def getConfig(binder):
        binder.bind(ExperimentModel, Injector.em)
        binder.bind(ExperimentConstants, Injector.ec)
        binder.bind(Kalman, Kalman(Injector.ec, Injector.em))
