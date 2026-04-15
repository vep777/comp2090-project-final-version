from heap import MinHeap
from radix_sort import radix_sort, radix_sort_with_steps


def heap_insert_demo():
    print("=== Heap Demo 1: Insert and Extract ===")
    heap = MinHeap()
    values = [42, 17, 8, 99, 23, 5]
    print(f"Insert values: {values}")

    for value in values:
        heap.insert(value)
        print(f"After inserting {value}: {heap}")

    print(f"Peek minimum: {heap.peek()}")
    print(f"Extract minimum: {heap.extract_min()}")
    print(f"Heap after extraction: {heap}")
    print()


def heap_build_demo():
    print("=== Heap Demo 2: Build Heap ===")
    values = [30, 12, 25, 7, 18, 40, 3]
    heap = MinHeap()
    heap.build_heap(values)

    print(f"Original values: {values}")
    print(f"Heap after build_heap(): {heap}")

    extracted = []
    while not heap.is_empty():
        extracted.append(heap.extract_min())

    print(f"Values extracted in order: {extracted}")
    print()


def radix_demo():
    print("=== Radix Sort Demo ===")
    numbers = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Original list: {numbers}")

    sorted_numbers, steps = radix_sort_with_steps(numbers)
    for label, step_result in steps:
        print(f"After sorting by {label} digit: {step_result}")

    print(f"Final sorted list: {sorted_numbers}")
    print()


def simple_check():
    print("=== Simple Check ===")
    numbers = [31, 14, 59, 26, 41]
    print(f"Original list: {numbers}")
    print(f"Sorted list:   {radix_sort(numbers)}")
    print()


if __name__ == "__main__":
    heap_insert_demo()
    heap_build_demo()
    radix_demo()
    simple_check()
