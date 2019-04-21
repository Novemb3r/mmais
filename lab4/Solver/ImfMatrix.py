import inject

from lab4.Experiment.ExperimentModel import ExperimentModel
from lab4.Experiment.ExperimentConstants import ExperimentConstants
from lab4.Kalman.Kalman import Kalman
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

        print(a)
        for i in range(self.const.m):
            a = np.vstack(a)

        print(a)

        result = a.reshape((self.const.m * (self.const.s + 1), self.const.m * (self.const.s + 1)))

        return result

    def imf_calc(self):
        M = 0

        for k in range(self.const.N):
            if k == 0:
                x_A_tk1 = np.array(
                    [np.dot(self.model.F(self.const.theta_0), self.model.mu_x(self.const.theta_0)) + self.const.a] +
                    [np.dot(self.model.F_grad(self.const.theta_0, i), self.model.mu_x(self.const.theta_0)) +
                     np.dot(self.model.F(self.const.theta_0), self.model.mu_x_grad(self.const.theta_0, i))
                     for i in range(self.const.s)]).T
                sigma_A_tk1 = np.zeros((self.const.s, self.const.s))

            else:

                # для многомерного случая
                # F_A_tk = [model.F(const.theta_0) + [np.zeros((const.m, const.m))] * const.s] + \
                #          [(model.F_grad(const.theta_0, i) - np.dot(kalman.K_hat_grad(const.theta_0, i),
                #                                                    model.H_grad(const.theta_0, i))) + [
                #               np.zeros((const.m, const.m))] * i + (
                #                   model.F(const.theta_0) - np.dot(kalman.K_hat(const.theta_0),
                #                                                   model.H(const.theta_0))) + np.zeros(
                #              (const.m, const.m)) * (const.s - i - 1) for i in range(const.s)]

                self.F_A_tk()
            # x_A_tk1 = np.dot(F_A_tk, x_mu_A_tk) + a_A_tk
            # sigma_A_tk1 = np.dot(np.dot(F_A_tk, sigma_A_tk1), F_A_tk.T) + np.dot(np.dot(K_A_tk, B_tk), K_A_tk.T)
            #
            # F_A_tk = np.hstack(([model.F] + [[np.zeros((const.s, const.s))] * const.s]) +
            #
            #                    [[model.F_grad(i) - K_w_tk @ model.H_grad(i)] + [model.F - K_w_tk @ model.H] +
            #                     [np.zeros((const.s, const.s))] * i +
            #                     [model.F - K_w_tk @ H_tk] + [np.zeros((const.s, const.s))] * (const.s - i)
            #                     for i in range(const.s)])