# User Guide - Task 2 Heap and Radix Sort

## 1. Requirements
- Python 3 installed on your computer
- All Task 2 files stored in the same folder

## 2. Files Needed
Make sure the following files are in the same folder:
- `heap.py`
- `radix_sort.py`
- `demo.py`

## 3. How to Run
Open a terminal in the Task 2 folder and run:

```bash
python demo.py
```

## 4. What the Demo Shows

### Heap Demo 1
This part demonstrates:
- inserting several values into the heap
- showing the heap after each insertion
- viewing the minimum value with `peek()`
- removing the minimum value with `extract_min()`

### Heap Demo 2
This part demonstrates:
- building a heap directly from an unsorted list with `build_heap()`
- extracting values one by one to show the heap order

### Radix Sort Demo
This part demonstrates:
- the original unsorted list
- the result after sorting by the ones digit
- the result after sorting by the tens digit
- the result after sorting by the hundreds digit
- the final sorted result

### Simple Check
This part uses another short list to show that the sorting function works correctly.

## 5. Notes
- This Radix Sort version only supports non-negative integers
- If negative integers are entered, the program will raise an error
