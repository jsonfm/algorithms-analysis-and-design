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
    # print()
    # print(result)
    result = array_to_number(result)
    return result


res = school_multiplication(5678, 1234)
print(res)
