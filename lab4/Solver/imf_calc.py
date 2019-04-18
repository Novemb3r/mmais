import inject

from lab4.Experiment.ExperimentModel import ExperimentModel
from lab4.Experiment.ExperimentConstants import ExperimentConstants
from lab4.Kalman.Kalman import Kalman
import numpy as np


def getF_A_tk(sha):


def imf_calc():
    const = inject.instance(ExperimentConstants)
    model = inject.instance(ExperimentModel)
    kalman = inject.instance(Kalman)

    M = 0

    for k in range(const.N):
        if k == 0:
            x_A_tk1 = np.array([np.dot(model.F(const.theta_0), model.mu_x(const.theta_0)) + const.a] +
                               [np.dot(model.F_grad(const.theta_0, i), model.mu_x(const.theta_0)) +
                                np.dot(model.F(const.theta_0), model.mu_x_grad(const.theta_0, i))
                                for i in range(const.s)]).T
            sigma_A_tk1 = np.zeros((const.s, const.s))

        else:

            # F_A_tk = [model.F(const.theta_0) + [np.zeros((const.m, const.m))] * const.s] + \
            #          [(model.F_grad(const.theta_0, i) - np.dot(kalman.K_hat_grad(const.theta_0, i),
            #                                                    model.H_grad(const.theta_0, i))) + [
            #               np.zeros((const.m, const.m))] * i + (
            #                   model.F(const.theta_0) - np.dot(kalman.K_hat(const.theta_0),
            #                                                   model.H(const.theta_0))) + np.zeros(
            #              (const.m, const.m)) * (const.s - i - 1) for i in range(const.s)]

            print(F_A_tk)
        # x_A_tk1 = np.dot(F_A_tk, x_mu_A_tk) + a_A_tk
        # sigma_A_tk1 = np.dot(np.dot(F_A_tk, sigma_A_tk1), F_A_tk.T) + np.dot(np.dot(K_A_tk, B_tk), K_A_tk.T)
        #
        # F_A_tk = np.hstack(([model.F] + [[np.zeros((const.s, const.s))] * const.s]) +
        #
        #                    [[model.F_grad(i) - K_w_tk @ model.H_grad(i)] + [model.F - K_w_tk @ model.H] +
        #                     [np.zeros((const.s, const.s))] * i +
        #                     [model.F - K_w_tk @ H_tk] + [np.zeros((const.s, const.s))] * (const.s - i)
        #                     for i in range(const.s)])
