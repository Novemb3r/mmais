import numpy as np

from lab4.Experiment.Experiment import ExperimentConstants
from lab4.Experiment.Experiment import ExperimentModel
from lab4.Helper import T, inv


class Kalman:

    def __init__(self, ec: ExperimentConstants, em: ExperimentModel):
        self.const = ec
        self.model = em

    def P_tk1_tk(self, theta):
        return np.dot(np.dot(self.model.F(theta), self.model.P_tk_tk(theta)), T(self.model.F(theta))) + \
               np.dot(np.dot(self.model.Gamma(theta), self.model.Q(theta)), T(self.model.Gamma(theta)))

    def B(self, theta):
        return np.dot(np.dot(self.model.H(theta), self.P_tk1_tk(theta)), T(self.model.H(theta))) + self.model.R(theta)

    def K(self, theta):
        return np.dot(np.dot(self.P_tk1_tk(theta), T(self.model.H(theta))), inv(self.B(theta)))

    def P_tk_tk(self, theta):
        return np.dot(np.eye(self.const.m) - np.dot(self.K(theta), self.model.H(theta)), self.P_tk1_tk(theta))

    def P_tk1_tk1(self, theta):
        return np.dot((np.eye(self.const.m) - np.dot(self.K(theta), self.model.H(theta))), self.P_tk1_tk(theta))

    def P_tk1_tk_grad(self, theta, i):
        return np.dot(np.dot(self.model.F_grad(theta, i), self.P_tk_tk(theta)), T(self.model.F(theta))) + \
               np.dot(np.dot(self.model.F(theta), self.model.P_tk_tk_grad(theta, i)), T(self.model.F(theta))) + \
               np.dot(np.dot(self.model.F(theta), self.model.P_tk_tk(theta)), self.model.F_grad(theta, i)) + \
               np.dot(np.dot(self.model.Gamma_grad(theta, i), self.model.Q(theta)), T(self.model.Gamma(theta))) + \
               np.dot(np.dot(self.model.Gamma(theta), self.model.Q_grad(theta, i)), T(self.model.Gamma(theta))) + \
               np.dot(np.dot(self.model.Gamma(theta), self.model.Q(theta)), T(self.model.Gamma_grad(theta, i)))

    def B_tk1_grad(self, theta, i):
        return np.dot(np.dot(self.model.H_grad(theta, i), self.P_tk1_tk(theta)), T(self.model.H(theta))) + \
               np.dot(np.dot(self.model.H(theta), self.P_tk1_tk_grad(theta, i)), T(self.model.H(theta))) + \
               np.dot(np.dot(self.model.H(theta), self.P_tk1_tk(theta)), T(self.model.H_grad(theta, i))) + \
               self.model.R_grad(theta, i)

    def K_tk1_grad(self, theta, i):
        return np.dot(np.dot(self.P_tk1_tk_grad(theta, i), T(self.model.H(theta))) +
                      np.dot(self.P_tk1_tk(theta), T(self.model.H_grad(theta, i))) -
                      np.dot(np.dot(np.dot(self.P_tk1_tk(theta), T(self.model.H(theta))), inv(self.B(theta))),
                             self.B_tk1_grad(theta, i)), inv(self.B(theta)))

    def P_tk1_tk1_grad(self, theta, i):
        return np.dot((np.eye(self.const.m) - np.dot(self.K(theta), self.model.H(theta))),
                      self.P_tk1_tk_grad(theta, i)) - \
               np.dot(np.dot(self.K_tk1_grad(theta, i), self.model.H(theta)) + np.dot(self.K(theta),
                                                                                      self.model.H_grad(theta, i)),
                      self.P_tk1_tk(theta))

    def K_hat(self, theta):
        return np.dot(self.model.F(theta), self.K(theta))

    def K_hat_grad(self, theta, i):
        return np.dot(self.model.F_grad(theta, i), self.K(theta)) + \
               np.dot(self.model.F(theta), self.K_tk1_grad(theta, i))
