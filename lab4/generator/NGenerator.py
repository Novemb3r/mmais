
import numpy as np

from lab4.model.model import Model


class NGenerator:

    def __init__(self, ec):
        self.ec = ec

    def generate(self):
        x_0 = np.random.multivariate_normal(self.ec.mu_x, self.ec.P_t0).T
        x = [x_0]
        for i in range(self.ec.N):
            w = np.random.multivariate_normal([0 for i in range(self.ec.m)], self.ec.Q).T
            x_t = Model.F(self.ec.theta_true) @ x[i] + Model.Psi(self.ec.theta_true) * self.ec.U[i] + w
            x.append(x_t)

        y = []
        for i in range(self.ec.N):
            v = np.random.multivariate_normal([0 for i in range(self.ec.m)], self.ec.R).T
            y_t = Model.A() + Model.H() @ x[1:][i] + v
            y.append(y_t)
        return y
