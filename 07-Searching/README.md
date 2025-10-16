# Searching Algorithms

## Overview
Searching is the process of finding a particular element in a collection of elements.

## Common Searching Algorithms

### 1. Linear Search
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- Works on unsorted data
- Simple but inefficient for large datasets

### 2. Binary Search
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1) iterative, O(log n) recursive
- Requires sorted data
- Very efficient for large datasets

### 3. Jump Search
- **Time Complexity**: O(√n)
- **Space Complexity**: O(1)
- Requires sorted data
- Better than linear search

### 4. Interpolation Search
- **Time Complexity**: O(log log n) average, O(n) worst
- **Space Complexity**: O(1)
- Requires sorted and uniformly distributed data
- Works best when data is uniformly distributed

### 5. Exponential Search
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- Requires sorted data
- Useful for unbounded/infinite arrays

## Files in this directory
- `searching_algorithms.py`: Implementation of all searching algorithms
