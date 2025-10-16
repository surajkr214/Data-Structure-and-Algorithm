# Sorting Algorithms

## Overview
Sorting is the process of arranging elements in a specific order (ascending or descending).

## Common Sorting Algorithms

### 1. Bubble Sort
- **Time Complexity**: O(n²) average and worst, O(n) best
- **Space Complexity**: O(1)
- **Stable**: Yes
- Simple but inefficient for large datasets

### 2. Selection Sort
- **Time Complexity**: O(n²) all cases
- **Space Complexity**: O(1)
- **Stable**: No
- Good for small datasets

### 3. Insertion Sort
- **Time Complexity**: O(n²) average and worst, O(n) best
- **Space Complexity**: O(1)
- **Stable**: Yes
- Efficient for small or nearly sorted data

### 4. Merge Sort
- **Time Complexity**: O(n log n) all cases
- **Space Complexity**: O(n)
- **Stable**: Yes
- Divide and conquer algorithm

### 5. Quick Sort
- **Time Complexity**: O(n log n) average, O(n²) worst
- **Space Complexity**: O(log n)
- **Stable**: No
- Very efficient in practice

### 6. Heap Sort
- **Time Complexity**: O(n log n) all cases
- **Space Complexity**: O(1)
- **Stable**: No
- Uses binary heap data structure

## Files in this directory
- `basic_sorting.py`: Bubble, Selection, Insertion sort
- `advanced_sorting.py`: Merge sort, Quick sort
