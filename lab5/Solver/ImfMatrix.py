import inject

from lab5.Experiment.ExperimentModel import ExperimentModel
from lab5.Experiment.ExperimentConstants import ExperimentConstants
from lab5.Helper import T, inv, combo_dot, TCD
from lab5.Kalman.Kalman import Kalman
import numpy as np


class ImfMatrix:

    def __init__(self):
        self.const = inject.instance(ExperimentConstants)
        self.model = inject.instance(ExperimentModel)
        self.kalman = inject.instance(Kalman)

    def F_A_tk(self):
        a = [[self.model.F(self.const.theta_0)] + [np.zeros((self.const.m, self.const.m))] * self.const.s] + \
            [[self.model.F_grad(self.const.theta_0, i) - np.dot(self.kalman.K_hat(self.const.theta_0),
                                                                self.model.H_grad(self.const.theta_0, i))] + [
                 np.zeros((self.const.m, self.const.m))] * i + [
                 self.model.F(self.const.theta_0) - np.dot(self.kalman.K_hat(self.const.theta_0),
                                                           self.model.H(self.const.theta_0))] + [
                 np.zeros((self.const.m, self.const.m))] * (self.const.s - i - 1) for i in range(0, self.const.s)]
        for i in range(self.const.m):
            a = np.hstack(a)

        result = a.reshape((self.const.m * (self.const.s + 1), self.const.m * (self.const.s + 1)))
        return result

    def a_A_tk(self):
        # # @TODO общий случай
        # return [self.const.a] + [
        #     self.a_gr(1)[i] - np.dot(self.kalman.K_hat(self.const.theta_0), self.model.A_grad(self.const.theta_0, i))
        #     for i
        #     in range(self.const.s)]
        return self.b_A_tk() + np.dot(self.Psi_A_tk(), self.const.U())

    def C(self, i):
        return np.reshape([np.zeros((self.const.m, self.const.m)) for _ in range(i + 1)] + [np.eye(self.const.m)] + [
            np.zeros((self.const.m, self.const.m)) for _ in range(self.const.s - i - 1)],
                          (self.const.m, self.const.m * (self.const.s + 1)))

    def K_A_tk(self):
        return np.reshape(
            [self.kalman.K_hat(self.const.theta_0)] + [self.kalman.K_hat_grad(self.const.theta_0, i) for i in
                                                       range(self.const.s)], (self.const.s + 1, self.const.m))

    def a(self):
        return self.model.b(self.const.theta_0) + np.dot(self.model.Psi(self.const.theta_0), self.const.U)

    def a_gr(self, k):
        return [self.model.b_grad(self.const.theta_0, i) + np.dot(self.model.Psi_grad(self.const.theta_0, i),
                                                                  self.const.U[k]) for i in range(self.const.s)]

    def Psi_A_tk(self):
        return [self.model.Psi(self.const.theta_0)] + [self.model.Psi_grad(self.const.theta_0, i) for i in
                                                       range(self.const.s)]

    def b_A_tk(self):
        return [self.model.b(self.const.theta_0)] + [
            self.model.b_grad(self.const.theta_0, i) - np.dot(self.kalman.K_hat(self.const.theta_0),
                                                              self.model.A_grad(self.const.theta_0, i)) for i in
            range(self.const.s)]

    def imf_calc(self):
        theta = self.const.theta_0

        M = np.zeros((self.const.s, self.const.s))
        for k in range(self.const.N):
            print(f"WE SURVIVED {k} ITERATIONS")

            self.const.a = np.dot(self.model.Psi(theta), self.const.U[k])
            a_gr = self.a_gr(k)

            if k == 0:
                x_A_tk1 = np.reshape([np.dot(self.model.F(theta), self.model.mu_x(theta)) + self.const.a] + \
                                     [np.dot(self.model.F_grad(theta, i), self.model.mu_x(theta)) +
                                      np.dot(self.model.F(theta), self.model.mu_x_grad(theta, i)) +
                                      a_gr[i]
                                      for i in range(self.const.s)], (self.const.s + 1, self.const.m))

                sigma_A_tk1 = np.zeros((self.const.s + 1, self.const.s + 1))

            E_x_hat = x_A_tk1
            E_x_hat_x_hat_t = sigma_A_tk1 + np.dot(x_A_tk1, T(x_A_tk1))
            for i in range(self.const.s):
                for j in range(self.const.s):
                    M[i][j] += TCD(self.model.H_grad(theta, i), self.C(0), E_x_hat_x_hat_t, T(self.C(0)),
                                   T(self.model.H_grad(theta, j)), inv(self.kalman.B(theta))) + \
                               TCD(self.model.H_grad(theta, i), self.C(0), E_x_hat_x_hat_t, T(self.C(j)),
                                   T(self.model.H(theta)), inv(self.kalman.B(theta))) + \
                               TCD(self.model.H_grad(theta, i), self.C(0), E_x_hat, T(self.model.A_grad(theta, j)),
                                   inv(self.kalman.B(theta))) + \
                               TCD(self.model.H(theta), self.C(i), E_x_hat_x_hat_t, T(self.C(0)),
                                   T(self.model.H_grad(theta, j)),
                                   inv(self.kalman.B(theta))) + \
                               TCD(self.model.H(theta), self.C(i), E_x_hat_x_hat_t, T(self.C(j)),
                                   T(self.model.H(theta)),
                                   inv(self.kalman.B(theta))) + \
                               TCD(self.model.H(theta), self.C(i), E_x_hat, T(self.model.A_grad(theta, j)),
                                   inv(self.kalman.B(theta))) + \
                               TCD(self.model.A_grad(theta, i), T(E_x_hat), T(self.C(0)),
                                   T(self.model.H_grad(theta, i)),
                                   inv(self.kalman.B(theta))) + \
                               TCD(self.model.A_grad(theta, i), T(E_x_hat), T(self.C(j)), T(self.model.H(theta)),
                                   inv(self.kalman.B(theta))) + \
                               TCD(self.model.A_grad(theta, i), T(self.model.A_grad(theta, j)),
                                   inv(self.kalman.B(theta))) + \
                               0.5 * TCD(self.kalman.B_tk1_grad(theta, i), inv(self.kalman.B(theta)),
                                         self.kalman.B_tk1_grad(theta, j), inv(self.kalman.B(theta)))

            if k != self.const.N - 1:
                x_A_tk1 = np.reshape((T(np.dot(self.F_A_tk(), x_A_tk1)) + self.a_A_tk()),
                                     (self.const.s + 1, self.const.m))

                sigma_A_tk1 = combo_dot(self.F_A_tk(), sigma_A_tk1, T(self.F_A_tk())) + combo_dot(self.K_A_tk(),
                                                                                                  self.kalman.B(theta),
                                                                                                  T(self.K_A_tk()))

                a = np.hstack(self.kalman.P_tk1_tk1(theta))[0]
                b = np.hstack([self.kalman.P_tk1_tk1_grad(theta, i) for i in range(self.const.s)])[0]

                self.kalman.model.P_tk_tk = lambda theta: a
                self.kalman.model.P_tk_tk_grad = lambda theta, i: b[i]

        return M

    def imf_calc_grad(self):
        s = self.const.s
        theta = self.const.theta_0

        imf_grad = np.zeros((s, s))
        P_tk_tk = self.const.P_t0

        M = np.zeros((self.const.s, self.const.s))

        for k in range(self.const.N):
            print(f"WE SURVIVED {k} ITERATIONS!")

            for beta in range(self.const.N):

                self.const.a = self.a()
                a_gr = self.a_gr(k)

                if k == 0:
                    x_A_tk1 = np.reshape([np.dot(self.model.F(theta), self.model.mu_x(theta)) + self.const.a] + \
                                         [np.dot(self.model.F_grad(theta, i), self.model.mu_x(theta)) +
                                          np.dot(self.model.F(theta), self.model.mu_x_grad(theta, i)) +
                                          a_gr[i]
                                          for i in range(self.const.s)], (self.const.s + 1, self.const.m))

                if beta == k:
                    # @todo
                    x_A_tk1_grad = 0
                else:
                    x_A_tk1_grad = np.zeros((self.const.s, self.const.s))

                for i in range(self.const.s):
                    for j in range(self.const.s):
                        M[i][j] += TCD(self.model.H_grad(theta, i), self.C(0), E_x_hat_x_hat_t, T(self.C(0)),
                                       T(self.model.H_grad(theta, j)), inv(self.kalman.B(theta))) + \
                                   TCD(self.model.H_grad(theta, i), self.C(0), E_x_hat_x_hat_t, T(self.C(j)),
                                       T(self.model.H(theta)), inv(self.kalman.B(theta))) + \
                                   TCD(self.model.H_grad(theta, i), self.C(0), E_x_hat, T(self.model.A_grad(theta, j)),
                                       inv(self.kalman.B(theta))) + \
                                   TCD(self.model.H(theta), self.C(i), E_x_hat_x_hat_t, T(self.C(0)),
                                       T(self.model.H_grad(theta, j)),
                                       inv(self.kalman.B(theta))) + \
                                   TCD(self.model.H(theta), self.C(i), E_x_hat_x_hat_t, T(self.C(j)),
                                       T(self.model.H(theta)),
                                       inv(self.kalman.B(theta))) + \
                                   TCD(self.model.H(theta), self.C(i), E_x_hat, T(self.model.A_grad(theta, j)),
                                       inv(self.kalman.B(theta))) + \
                                   TCD(self.model.A_grad(theta, i), T(E_x_hat), T(self.C(0)),
                                       T(self.model.H_grad(theta, i)),
                                       inv(self.kalman.B(theta))) + \
                                   TCD(self.model.A_grad(theta, i), T(E_x_hat), T(self.C(j)), T(self.model.H(theta)),
                                       inv(self.kalman.B(theta)))

                if k != self.const.N - 1:
                    x_A_tk1 = np.reshape((T(np.dot(self.F_A_tk(), x_A_tk1)) + self.a_A_tk()),
                                         (self.const.s + 1, self.const.m))

                    a = np.hstack(self.kalman.P_tk1_tk1(theta))[0]
                    b = np.hstack([self.kalman.P_tk1_tk1_grad(theta, i) for i in range(self.const.s)])[0]

                    self.kalman.model.P_tk_tk = lambda theta: a
                    self.kalman.model.P_tk_tk_grad = lambda theta, i: b[i]

        return M
