def merge_sort(array: list):
    if len(array) > 1:
        n = len(array) // 2
        left = array[:n]
        right = array[n:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            # print(f"(1) left [i={i}] = ", left[i], f" || right[j={j}]", right[j])
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            # print(f"(2) left[i={i}] = ", left[i])
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

        return array


# array = [12, 10, 13, 5, 6, 7, 2]
# print("input: ", array)
# merge_sort(array)
# print(array)

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    from performance import time_performance_recursive_v2
    from utils import generate_array_of_arrays

    L = 1000
    arrays = generate_array_of_arrays(max_array_length=L)
    times = time_performance_recursive_v2(merge_sort, arrays)

    on_real = 1000 * np.array(times)  # ms

    n = list(range(1, L))
    coefs = np.polyfit(n, times, 1)
    fit = np.poly1d(coefs)
    on_ideal = 1000 * fit(n)
    str_fit = str(fit).replace("x", "n")
    plt.plot(n, on_real, label="real O(n)")
    plt.plot(n, on_ideal, label=f"aprox. O(n) = {str_fit}")
    plt.xlabel("Array Length")
    plt.ylabel("time (ms)")
    plt.title("Merge Sort Algorithm")
    plt.grid()
    plt.legend()
    plt.show()
