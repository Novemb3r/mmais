import numpy as np


def T(arg):
    if type(arg).__module__ == np.__name__:
        return arg.T

    return np.array(arg).T


def inv(arg):

    if type(arg).__module__ == np.__name__ and arg.shape != ():
        return np.linalg.inv(arg)

    if isinstance(arg, list):
        arg = np.array(arg)
        if arg.ndim != 1:
            return inv(arg)

    return 1.0 / arg


def trace(arg):
    if type(arg).__module__ == np.__name__ and arg.shape != ():
        return np.trace(arg)

    if isinstance(arg, list):
        arg = np.array(arg)
        if arg.ndim != 1:
            return trace(arg)

    return arg


def combo_dot(*args):
    acc = args[0]

    for i in args[1:]:
        acc = np.dot(acc, i)

    return acc


def TCD(*args):
    return trace(combo_dot(*args))
