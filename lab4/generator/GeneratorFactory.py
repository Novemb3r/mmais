from lab4.generator.NGenerator import NGenerator
from lab4.generator.OneGenerator import OneGenerator


def get(n, experiment_model, experiment_constants):
    return {
        n < 2: OneGenerator(experiment_model, experiment_constants),
        n >= 2: NGenerator(experiment_model, experiment_constants)
    }[True]
