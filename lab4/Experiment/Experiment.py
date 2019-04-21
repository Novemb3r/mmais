from lab4.Experiment.ExperimentConstants import ExperimentConstants
from lab4.Experiment.ExperimentModel import ExperimentModel


class Experiment:
    ec = ExperimentModel(
        Psi=lambda theta: theta[1],
        A=lambda theta: 0,
        H=lambda theta: 1,
        Q=lambda theta: 0.1,
        R=lambda theta: 0.3,
        mu_x=lambda theta: 0,
        F=lambda theta: theta[0],
        Gamma=lambda theta: 1,
        P_tk_tk=lambda theta: 0.1,

        Psi_grad=[
            lambda theta: 0,
            lambda theta: 1,
        ],
        R_grad=[
            lambda theta: 0,
            lambda theta: 0,
        ],
        Q_grad=[
            lambda theta: 0,
            lambda theta: 0,
        ],
        A_grad=[
            lambda theta: 0,
            lambda theta: 0,
        ],
        H_grad=[
            lambda theta: 0,
            lambda theta: 0,
        ],
        F_grad=[
            lambda theta: 1,
            lambda theta: 0,
        ],
        Gamma_grad=[
            lambda theta: 0,
            lambda theta: 0,
        ],
        mu_x_grad=[
            lambda theta: 0,
            lambda theta: 0,
        ],
        P_tk_tk_grad=[
            lambda theta: 0,
            lambda theta: 0,
        ],
    )

    em = ExperimentConstants(
        P_t0=0.1,
        theta_0=[1, 1],
        theta_true=[1, 1],
        m=1,
        N=2,
        a=2,
        s=2,
    )

    @staticmethod
    def get():
        return Experiment.ec, Experiment.em
