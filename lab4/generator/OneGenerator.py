import numpy as np


class OneGenerator:

    def __init__(self, em, ec):
        self.ec = ec
        self.em = em

    def generate(self):
        x_0 = np.random.normal(self.ec.mu_x, self.ec.P_t0)
        x = [x_0]
        for i in range(self.ec.N):
            w = float(np.random.normal([0 for i in range(self.ec.m)], self.ec.Q))
            x_t = self.em.F(self.ec.theta_true) * x[i] + self.em.Psi(self.ec.theta_true) * self.ec.U[i] + w
            x.append(x_t)

        y = []
        for i in range(self.ec.N):
            v = float(np.random.normal([0 for i in range(self.ec.m)], self.ec.R))
            y_t = self.em.A() + self.em.H() * x[1:][i] + v
            y.append(y_t)
        return y
