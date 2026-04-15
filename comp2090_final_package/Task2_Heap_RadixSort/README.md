# Task 2 - Self-study on Heap and Radix Sort

## Selected topics
- **New data structure**: Heap (Min Heap)
- **New algorithm**: Radix Sort

## Why these topics were selected
Heap and Radix Sort are suitable topics for this project because they are practical, not too difficult for an introductory course, and easy to explain with simple Python code.

## Data structure: Heap
A heap is a complete binary tree that satisfies the heap property. In a **min heap**, the parent node is always smaller than or equal to its child nodes.

### Main operations
- `insert(value)`
- `extract_min()`
- `peek()`
- `is_empty()`
- `build_heap(values)`

### Applications
- Priority queue
- Task scheduling
- Shortest path algorithms
- Event simulation

### Time complexity
- Insert: `O(log n)`
- Extract minimum: `O(log n)`
- Peek: `O(1)`
- Build heap: `O(n)`

## Algorithm: Radix Sort
Radix sort is a non-comparison sorting algorithm. It sorts numbers digit by digit. In this project, the least-significant-digit version is used.

### Time complexity
A common form is `O(d(n + k))`, where:
- `d` = number of digits
- `n` = number of elements
- `k` = range of each digit, which is 10 in decimal digits

### Advantages
- Efficient for sorting non-negative integers with limited digit length
- Can be faster than comparison-based sorting in some cases

### Limitations
- This beginner version only supports non-negative integers
- It is less flexible for general-purpose data types

## Files
- `heap.py` - implementation of min heap
- `radix_sort.py` - implementation of radix sort
- `demo.py` - demonstration file
- `USER_GUIDE.md` - how to run the program

## How to run
```bash
python demo.py
```
