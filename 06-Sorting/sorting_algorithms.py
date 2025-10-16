"""
Sorting Algorithms
Implementation of common sorting algorithms with examples.
"""


def bubble_sort(arr):
    """
    Bubble Sort: Repeatedly swap adjacent elements if they're in wrong order.
    
    Time Complexity: O(n²) average and worst case, O(n) best case
    Space Complexity: O(1)
    Stable: Yes
    """
    n = len(arr)
    arr = arr.copy()  # Don't modify original
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping happened, array is sorted
        if not swapped:
            break
    
    return arr


def selection_sort(arr):
    """
    Selection Sort: Find minimum element and place it at beginning.
    
    Time Complexity: O(n²) all cases
    Space Complexity: O(1)
    Stable: No
    """
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        # Find minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap minimum element with first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def insertion_sort(arr):
    """
    Insertion Sort: Build sorted array one element at a time.
    
    Time Complexity: O(n²) average and worst case, O(n) best case
    Space Complexity: O(1)
    Stable: Yes
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


def merge_sort(arr):
    """
    Merge Sort: Divide and conquer algorithm.
    
    Time Complexity: O(n log n) all cases
    Space Complexity: O(n)
    Stable: Yes
    """
    if len(arr) <= 1:
        return arr
    
    # Divide array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge sorted halves
    return merge(left, right)


def merge(left, right):
    """Helper function to merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def quick_sort(arr):
    """
    Quick Sort: Pick a pivot and partition array around it.
    
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n)
    Stable: No
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def counting_sort(arr):
    """
    Counting Sort: Non-comparison based sorting for integers.
    
    Time Complexity: O(n + k) where k is range of input
    Space Complexity: O(k)
    Stable: Yes
    
    Note: Only works for non-negative integers
    """
    if not arr:
        return arr
    
    # Find the range
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    # Create count array
    count = [0] * range_val
    output = [0] * len(arr)
    
    # Store count of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Change count[i] to contain actual position
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output


# Example usage and comparison
if __name__ == "__main__":
    import time
    
    # Test data
    test_arrays = {
        "Small Random": [64, 34, 25, 12, 22, 11, 90],
        "Nearly Sorted": [1, 2, 3, 5, 4, 6, 7, 8, 9],
        "Reverse Sorted": [9, 8, 7, 6, 5, 4, 3, 2, 1],
        "All Same": [5, 5, 5, 5, 5],
    }
    
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Counting Sort": counting_sort,
    }
    
    for array_name, test_array in test_arrays.items():
        print(f"\n=== {array_name}: {test_array} ===")
        
        for algo_name, algo_func in algorithms.items():
            arr_copy = test_array.copy()
            start = time.perf_counter()
            sorted_arr = algo_func(arr_copy)
            end = time.perf_counter()
            
            print(f"{algo_name:20}: {sorted_arr} ({(end-start)*1000000:.2f} μs)")
