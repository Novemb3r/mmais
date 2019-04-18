import inject
import numpy as np

from lab4.Experiment.ExperimentConstants import ExperimentConstants
from lab4.Experiment.ExperimentModel import ExperimentModel


class NGenerator:

    def __init__(self):
        self.ec = inject.instance(ExperimentConstants)
        self.em = inject.instance(ExperimentModel)

    def generate(self):
        x_0 = np.random.multivariate_normal(self.em.mu_x(0), self.ec.P_t0).T
        x = [x_0]
        for i in range(self.ec.N):
            w = np.random.multivariate_normal([0 for i in range(self.ec.m)], self.ec.Q).T
            x_t = self.em.F(self.ec.theta_true) @ x[i] + self.em.Psi(self.ec.theta_true) * self.ec.U[i] + w
            x.append(x_t)

        y = []
        for i in range(self.ec.N):
            v = np.random.multivariate_normal([0 for i in range(self.ec.m)], self.ec.R).T
            y_t = self.em.A() + self.em.H() @ x[1:][i] + v
            y.append(y_t)
        return y
