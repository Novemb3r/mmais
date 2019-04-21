from lab4.tests.test_Helpers.fixtures import *
import numpy as np

from lab4.Helper import T


# ===============================================


def test_T_1():
    assert np.array_equal(T(1), 1)


def test_T_2():
    assert np.array_equal(T([1]), [1])


def test_T_3():
    assert np.array_equal(T([1, 2]), [1, 2])


def test_T_4():
    assert np.array_equal(T(a), a_t)


def test_T_5():
    assert np.array_equal(T(npa), npa_t)

# ===============================================
