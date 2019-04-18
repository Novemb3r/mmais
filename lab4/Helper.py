import numpy as np


def T(arg):
    if type(arg).__module__ == np.__name__:
        return arg.T

    return arg


def inv(arg):
    if type(arg).__module__ == np.__name__ and arg.shape != ():
        return np.linalg.inv(arg)

    return 1.0 / arg
