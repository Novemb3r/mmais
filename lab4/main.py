from lab4.Experiment.Experiment import Experiment
from lab4.Injector import Injector
from lab4.Solver.ImfMatrix import ImfMatrix
import numpy as np

def main():
    ec, em = Experiment.get()

    Injector.setParams(ec, em).configure()

    # y = GeneratorFactory.get(1).generate()

    IMF = ImfMatrix()

    M = IMF.imf_calc()

    print(f'ИМФ:\n{M}')
    print(f'Обратная ИМФ:\n{np.linalg.inv(M)}')
    print(f'sp(M^-1)): {np.trace(np.linalg.inv(M))}')
    print(f'det(M^-1): {np.linalg.det(np.linalg.inv(M))}')



if __name__ == '__main__':
    main()
