from lab4.generator import GeneratorFactory
from lab4.ExperimentConstants import ExperimentConstants
from lab4.model.ExperimentModel import ExperimentModel
from lab4.solver.imf_calc import imf_calc


def main():
    a1 = ExperimentConstants(
        P_t0=0.1,
        theta_0=[0.1, 0.1],
        theta_true=[1, 1],
        R=0.3,
        Q=0.1,
        m=1,
        N=2,
        a=0,
        s=2,
    )

    m1 = ExperimentModel(
        Psi=lambda theta: theta[1],
        A=lambda theta: 0,
        H=lambda theta: 1,
        mu_x=lambda theta: 0,
        F=lambda theta: theta[0],
        Gamma=lambda theta: 1,
        P_tk_tk=lambda theta: 0.1,

        Psi_grad=[
            lambda theta: 0,
            lambda theta: 1,
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

    imf_calc(a1, m1)

    #
    # a2 = ExperimentConstants(P_t0=[[0.05, 0], [0, 0.05]],
    #                          mu_x=[-5, 0],
    #                          theta_0=[0.1, 0.1],
    #                          theta_true=[1, -1],
    #                          R=[[0.3, 0], [0, 0.3]],
    #                          Q=[[0.1, 0], [0, 0.1]],
    #                          m=2,
    #                          N=10,
    #                          )
    #
    y = GeneratorFactory.get(1, m1, a1).generate()

    # y = GeneratorFactory.get(2, a2).generate()

    print(y)



if __name__ == '__main__':
    main()
