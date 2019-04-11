from lab4.generator import GeneratorFactory
from lab4.ExperimentConstants import ExperimentConstants
from lab4.model.ExperimentModel import ExperimentModel


def main():
    # consts = ExperimentConstants(Pt0 = 0.1, mu_x = 0, Q = 0.2)
    # print(consts)
    # GeneratorFactory.get(3)
    # theta=[1, -1]
    # Psi = [[theta[0], 2],
    #       [3, theta[1]]]
    #
    # a = lambda x: []
    # print(Psi)
    #
    # asbdsakdl = Model(a)
    #
    # print(asbdsakdl.Psi([2, 3]))

    m1 = ExperimentModel(
        Psi=lambda theta: theta[1],
        A=lambda: 0,
        H=lambda: 1,
        F=lambda theta: theta[0]
    )

    a1 = ExperimentConstants(P_t0=0.1,
                             mu_x=0,
                             theta_0=[0.1, 0.1],
                             theta_true=[1, 1],
                             R=0.3,
                             Q=0.1,
                             m=1,
                             N=10,
                             )
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
