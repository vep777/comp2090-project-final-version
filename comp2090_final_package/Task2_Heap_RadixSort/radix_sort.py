def radix_sort(numbers):
    """Least-significant-digit radix sort for non-negative integers."""
    if not numbers:
        return []
    if any(n < 0 for n in numbers):
        raise ValueError("This simple version only supports non-negative integers.")

    result = list(numbers)
    max_value = max(result)
    exp = 1

    while max_value // exp > 0:
        result = _counting_sort_by_digit(result, exp)
        exp *= 10

    return result


def _counting_sort_by_digit(numbers, exp):
    output = [0] * len(numbers)
    count = [0] * 10

    for number in numbers:
        digit = (number // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(len(numbers) - 1, -1, -1):
        digit = (numbers[i] // exp) % 10
        output[count[digit] - 1] = numbers[i]
        count[digit] -= 1

    return output
