import numpy as np
import pytest

from lab4.Helper import T

a = [[0, 1], [2, 3]]
a_t = [[0, 2], [1, 3]]

b = [[3, 4], [5, 6]]
c = [[7, 8], [9, 10]]
d = [[11, 12], [13, 14]]


def test_T_1():
    assert np.array_equal(T(1), 1)


def test_T_2():
    assert np.array_equal(T([1]), [1])


def test_T_3():
    assert np.array_equal(T([1, 2]), [1, 2])


def test_T_4():
    assert np.array_equal(T(a), a_t)
