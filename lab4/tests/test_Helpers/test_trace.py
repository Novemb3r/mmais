from lab4.tests.test_Helpers.fixtures import *
import numpy as np

from lab4.Helper import trace


# ===============================================


def test_T_1():
    assert trace(1) == 1


def test_T_2():
    assert trace([1]) == [1]


def test_T_4():
    assert trace(a) == a_tr


def test_T_5():
    assert trace(npa) == npa_tr

# ===============================================
