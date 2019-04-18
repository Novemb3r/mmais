from lab4.Generator.NGenerator import NGenerator
from lab4.Generator.OneGenerator import OneGenerator


def get(n):
    return {
        n < 2: OneGenerator(),
        n >= 2: NGenerator()
    }[True]
