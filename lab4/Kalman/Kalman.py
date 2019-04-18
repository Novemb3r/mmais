import numpy as np
import inject

from lab4.ExperimentConstants import ExperimentConstants
from lab4.Helpers import Helpers
from lab4.model.ExperimentModel import ExperimentModel


class Kalman:

    def __init__(self):
        self.const = inject.instance(ExperimentConstants)
        self.model = inject.instance(ExperimentModel)

    def P_tk1_tk(self, theta):
        return np.dot(np.dot(self.model.F(theta), self.model.P_tk_tk(theta)), self.model.F(theta).T) + \
               np.dot(np.dot(self.model.Gamma(theta), self.const.Q), self.model.Gamma(theta).T)

    def B(self, theta):
        return np.dot(np.dot(self.model.H(theta), self.P_tk1_tk(theta)), self.model.H(theta).T) + self.const.R

    def K(self, theta):
        return np.dot(np.dot(self.P_tk1_tk(theta), self.model.H(theta).T), np.linalg.inv(self.B(theta)))

    def P_tk_tk(self, theta):
        return np.dot(np.eye(self.const.m) - np.dot(self.K(theta), self.model.H(theta)), self.P_tk1_tk(theta))

    def P_tk1_tk_grad(self, theta, i):
        return np.dot(np.dot(self.model.F_grad(theta, i), self.P_tk_tk(theta)), self.model.F(theta).T) + \
               np.dot(self.model.F(theta), 
