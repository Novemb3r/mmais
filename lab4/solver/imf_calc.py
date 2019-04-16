from lab4.model.ExperimentModel import ExperimentModel
from lab4.ExperimentConstants import ExperimentConstants
import numpy as np


def imf_calc(const: ExperimentConstants, model: ExperimentModel):
    for k in range(const.N):
        if k == 0:
            x_A_tk1 = np.array([model.F + const.mu_x + const.a] +
                               [model.F_grad(i) @ const.mu_x +
                                model.F @ model.mu_x_grad(i) +
                                model.a_grad(i) for i in range(const.s)]).T
            sigma_A_tk1 = np.zeros((const.s, const.s))

        else:
            x_A_tk1 = F_A_tk @ x_mu_A_tk + a_A_tk
            sigma_A_tk1 = F_A_tk @ sigma_A_tk1 @ F_A_tk.T + K_A_tk @ B_tk @ K_A_tk.T

            F_A_tk = np.hstack(([model.F] + [[np.zeros((const.s, const.s))] * const.s]) +

                               [[model.F_grad(i) - K_w_tk @ model.H_grad(i)] + [model.F - K_w_tk @ model.H] +
                                [np.zeros((const.s, const.s))] * i +
                                [model.F - K_w_tk @ H_tk] + [np.zeros((const.s, const.s))] * (const.s - i)
                                for i in range(const.s)])
