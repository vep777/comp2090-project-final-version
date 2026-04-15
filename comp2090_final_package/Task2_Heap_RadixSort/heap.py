class MinHeap:
    """Simple array-based min heap implementation."""

    def __init__(self):
        self._data = []

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty.")
        return self._data[0]

    def insert(self, value):
        self._data.append(value)
        self._heapify_up(len(self._data) - 1)

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Heap is empty.")
        if len(self._data) == 1:
            return self._data.pop()

        root = self._data[0]
        self._data[0] = self._data.pop()
        self._heapify_down(0)
        return root

    def build_heap(self, values):
        self._data = list(values)
        for i in range(len(self._data) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self._data[index] < self._data[parent]:
                self._data[index], self._data[parent] = self._data[parent], self._data[index]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self._data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self._data[left] < self._data[smallest]:
                smallest = left
            if right < size and self._data[right] < self._data[smallest]:
                smallest = right

            if smallest == index:
                break

            self._data[index], self._data[smallest] = self._data[smallest], self._data[index]
            index = smallest

    def __str__(self):
        return f"MinHeap({self._data})"
