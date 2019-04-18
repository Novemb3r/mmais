import inject
import numpy as np

from lab4.ExperimentConstants import ExperimentConstants
from lab4.model.ExperimentModel import ExperimentModel


class OneGenerator:

    def __init__(self):
        self.ec = inject.instance(ExperimentConstants)
        self.em = inject.instance(ExperimentModel)

    def generate(self):
        x_0 = np.random.normal(self.em.mu_x(0), self.ec.P_t0)
        x = [x_0]
        for i in range(self.ec.N):
            w = float(np.random.normal([0 for i in range(self.ec.m)], self.ec.Q))
            x_t = self.em.F(self.ec.theta_true) * x[i] + self.em.Psi(self.ec.theta_true) * self.ec.U[i] + w
            x.append(x_t)

        y = []
        for i in range(self.ec.N):
            v = float(np.random.normal([0 for i in range(self.ec.m)], self.ec.R))
            y_t = self.em.A(0) + self.em.H(0) * x[1:][i] + v
            y.append(y_t)
        return y
