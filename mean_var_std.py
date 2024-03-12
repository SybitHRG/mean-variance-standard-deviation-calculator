import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    matrix = np.reshape(list, (3, 3))

    calculations = {
        'mean': execute_by_axis_and_flatten(matrix.mean),
        'variance': execute_by_axis_and_flatten(matrix.var),
        'standard deviation': execute_by_axis_and_flatten(matrix.std),
        'max': execute_by_axis_and_flatten(matrix.max),
        'min': execute_by_axis_and_flatten(matrix.min),
        'sum': execute_by_axis_and_flatten(matrix.sum)
    }
    # print(list)
    # print(matrix)
    # print(calculations)
    return calculations


def execute_by_axis_and_flatten(function):
    return [function(axis=0).tolist(), function(axis=1).tolist(), function()]
