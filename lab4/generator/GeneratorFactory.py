from lab4.generator.NGenerator import NGenerator
from lab4.generator.OneGenerator import OneGenerator


def get(n):
    return {
        n < 2: OneGenerator(),
        n >= 2: NGenerator()
    }[True]
