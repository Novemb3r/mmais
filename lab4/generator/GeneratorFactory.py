from lab4.generator.NGenerator import NGenerator
from lab4.generator.OneGenerator import OneGenerator


def get(n, experiment_constants):
    return {
        n < 2: OneGenerator(experiment_constants),
        n >= 2: NGenerator(experiment_constants)
    }[True]
