# Task 2 - Heap and Radix Sort

## Overview
This task is the self-study part of the project. It introduces one new data structure and one new algorithm beyond the basic course materials.

Selected topics:
- **Min Heap** as the new data structure
- **Radix Sort** as the new algorithm

## Files
- `heap.py` - Min Heap implementation
- `radix_sort.py` - Radix Sort implementation
- `demo.py` - demonstration program

## Topic Summary

### Min Heap
The Min Heap is implemented using a Python list. It supports the following operations:
- `insert(value)`
- `extract_min()`
- `peek()`
- `is_empty()`
- `build_heap(values)`

### Radix Sort
The Radix Sort implementation uses the least-significant-digit method for non-negative integers. A helper function is also included to display the intermediate results after each digit pass.

## Demonstration
The demo program shows:
- heap insertion and extraction
- heap construction using `build_heap()`
- radix sort step-by-step output
- a simple correctness check

## How to Run
Please see `USER_GUIDE.md` for the running instructions.
