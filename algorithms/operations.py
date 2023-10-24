def school_multiplication(a, b, verbose=False):
    """Multiplication of two integers using the standard multiplication algorithm.
       a
    x  b
    ______
    result
    """

    def obtain_digits(num):
        return [int(digit) for digit in str(num)]

    def array_to_number(array):
        string = ""
        for number in array:
            string += f"{number}"
        result = int(string)
        return result

    def append_number_digits(number, array):
        digits = obtain_digits(number)[::-1]
        for digit in digits:
            array.append(digit)
        return array

    a = obtain_digits(a)
    b = obtain_digits(b)

    # print(a)
    # print(b)
    # print()

    a = a[::-1]
    b = b[::-1]
    rows = []

    for i in range(len(b)):
        row = [0 for i in range(i)]
        # row = []
        next_digit_sum = 0

        for j in range(len(a)):
            r = b[i] * a[j] + next_digit_sum
            r_digits = obtain_digits(r)

            # if verbose:
            # print(f"{b[i]} x {a[j]} = {r_digits[-1]} (+{next_digit_sum})")
            if len(r_digits) > 1:
                without_last_digit = r_digits[:-1]
                next_digit_sum = array_to_number(without_last_digit)

            if j < len(a) - 1:
                r = r_digits[-1]
                row.append(r)

            if j >= len(a) - 1:
                row = append_number_digits(r, row)

        row = row[::-1]

        for _ in range(len(a) - i):
            row.insert(0, 0)

        if len(row) <= len(a) + len(b) + 1:
            for _ in range(len(a) + len(b) + 1 - len(row)):
                row.insert(0, 0)
        # print(row)
        rows.append(row)

    result = []
    next_carry = 0

    for i in range(len(a) + len(b) + 1):
        sum_ = 0
        string = ""

        for index, row in enumerate(rows):
            row = row[::-1]
            sum_ += row[i]
            if index < len(rows) - 1:
                string += f"{row[i]} + "
            else:
                string += f"{row[i]}"

        sum_ += next_carry
        string += f" = {sum_}"
        sum_digits = obtain_digits(sum_)
        last_sum_digit = sum_digits[-1]

        if len(sum_digits) > 1:
            without_last_digit = sum_digits[:-1]
            next_carry = array_to_number(without_last_digit)
        else:
            next_carry = 0

        string += f" (+{next_carry})"
        result.append(last_sum_digit)

    result = result[::-1]
    result = array_to_number(result)
    return result


# res = school_multiplication(5678, 1234)
# print(res)
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    from performance import time_performance_recursive
    from utils import generate_random_inputs

    L = 100

    inputs = generate_random_inputs(input_length=2, number_of_inputs=L)
    times = time_performance_recursive(school_multiplication, inputs)
    on_real = 1000 * np.array(times)

    n = list(range(1, L))
    coefs = np.polyfit(n, times, 2)
    fit = np.poly1d(coefs)
    on_ideal = 1000 * fit(n)

    plt.plot(n, on_real, label="Real O(n) = $n^2$")
    plt.plot(n, on_ideal, label="expected O(n) = $n^2$")
    plt.grid()
    plt.ylabel("time (ms)")
    plt.xlabel("N length")
    plt.title("School Multiplication Algorithm")
    plt.legend()
    plt.show()
