from lab4.generator import GeneratorFactory
from lab4.experimentConstants import ExperimentConstants


def main():
    # consts = ExperimentConstants(Pt0 = 0.1, mu_x = 0, Q = 0.2)
    # print(consts)
    # GeneratorFactory.get(3)

    a1 = ExperimentConstants(P_t0=0.1,
                             mu_x=0,
                             theta_0=[0.1, 0.1],
                             theta_true=[1, 1],
                             R=0.3,
                             Q=0.1,
                             m=1,
                             N=10,
                             )

    a2 = ExperimentConstants(P_t0=[[0.05, 0], [0, 0.05]],
                             mu_x=[-5, 0],
                             theta_0=[0.1, 0.1],
                             theta_true=[1, -1],
                             R=[[0.3, 0], [0, 0.3]],
                             Q=[[0.1, 0], [0, 0.1]],
                             m=2,
                             N=10,
                             )

    # y = GeneratorFactory.get(1, a1).generate()

    y = GeneratorFactory.get(2, a2).generate()

    print(y)


if __name__ == '__main__':
    main()
