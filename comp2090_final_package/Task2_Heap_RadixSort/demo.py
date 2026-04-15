from heap import MinHeap
from radix_sort import radix_sort


def heap_demo():
    print("=== Heap Demo ===")
    heap = MinHeap()
    values = [42, 17, 8, 99, 23, 5]
    print(f"Insert values: {values}")

    for value in values:
        heap.insert(value)
        print(f"After inserting {value}: {heap}")

    print(f"Peek minimum value: {heap.peek()}")
    print(f"Extract minimum value: {heap.extract_min()}")
    print(f"Heap after extraction: {heap}")
    print()


def radix_demo():
    print("=== Radix Sort Demo ===")
    numbers = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Original list: {numbers}")
    print(f"Sorted list: {radix_sort(numbers)}")
    print()


if __name__ == "__main__":
    heap_demo()
    radix_demo()
