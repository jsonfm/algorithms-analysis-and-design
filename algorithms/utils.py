import random


def generate_random_array(length=2, min_value=10, max_value=30):
    array = [random.randint(min_value, max_value) for _ in range(length)]
    return array


def generate_random_inputs(input_length=2, number_of_inputs=100):
    inputs = []
    for i in range(1, number_of_inputs):
        min_ = 10 ** (i - 1)
        max_ = 10**i
        inputs.append(generate_random_array(input_length, min_, max_))
    return inputs


def generate_array_of_arrays(
    min_array_length=1, max_array_length=100, number_of_arrays=100
):
    arrays = []
    for array_length in range(1, max_array_length):
        array = generate_random_array(array_length, min_value=10, max_value=100)
        arrays.append(array)
    return arrays
