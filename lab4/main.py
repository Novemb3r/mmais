from lab4.Experiment.Experiment import Experiment
from lab4.Generator import GeneratorFactory
from lab4.Injector import Injector
from lab4.Solver.imf_calc import imf_calc


def main():
    ec, em = Experiment.get()

    Injector.setParams(ec, em).configure()

    # y = GeneratorFactory.get(1).generate()

    imf_calc()

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

    # y = GeneratorFactory.get(2, a2).generate()


#


if __name__ == '__main__':
    main()
