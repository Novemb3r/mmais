from lab4.tests.test_Helpers.fixtures import *
import numpy as np

from lab4.Helper import inv


# ===============================================


def test_T_1():
    assert np.array_equal(inv(2), 0.5)


def test_T_2():
    assert np.array_equal(inv([2]), [0.5])


def test_T_3():
    assert np.array_equal(inv([1, 2]), [1, 0.5])


def test_T_4():
    assert np.array_equal(inv(a), a_inv)

def test_T_5():
    assert np.array_equal(inv(npa), npa_inv)

# ===============================================
