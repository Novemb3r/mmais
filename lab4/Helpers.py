import numpy as np
import sympy as sp


class Helpers:

    # @TODO realize for more thetas

    @staticmethod
    def gradient(value, sTheta):

        sTheta = [
            sp.Symbol('theta[0]'),
            sp.Symbol('theta[1]')
        ]


        return [np.diff(value, sTheta[0]), np.diff(value, sTheta[1])]
