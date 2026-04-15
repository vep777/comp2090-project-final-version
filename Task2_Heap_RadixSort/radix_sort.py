def radix_sort(numbers):
    """Least-significant-digit radix sort for non-negative integers."""
    if not numbers:
        return []
    if any(n < 0 for n in numbers):
        raise ValueError("This version only supports non-negative integers.")

    result = list(numbers)
    max_value = max(result)
    exp = 1

    while max_value // exp > 0:
        result = _counting_sort_by_digit(result, exp)
        exp *= 10

    return result


def radix_sort_with_steps(numbers):
    """Return the sorted list and intermediate results after each digit pass."""
    if not numbers:
        return [], []
    if any(n < 0 for n in numbers):
        raise ValueError("This version only supports non-negative integers.")

    result = list(numbers)
    steps = []
    max_value = max(result)
    exp = 1
    place_names = {1: "ones", 10: "tens", 100: "hundreds", 1000: "thousands"}

    while max_value // exp > 0:
        result = _counting_sort_by_digit(result, exp)
        label = place_names.get(exp, f"10^{len(str(exp)) - 1} place")
        steps.append((label, list(result)))
        exp *= 10

    return result, steps


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
