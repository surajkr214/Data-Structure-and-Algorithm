"""
Searching Algorithms
Implementation of common searching algorithms with examples.
"""

import math


def linear_search(arr, target):
    """
    Linear Search: Check each element sequentially.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr: List to search in
        target: Element to find
    
    Returns:
        Index of element or -1 if not found
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search_iterative(arr, target):
    """
    Binary Search (Iterative): Divide and conquer on sorted array.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Args:
        arr: Sorted list to search in
        target: Element to find
    
    Returns:
        Index of element or -1 if not found
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Binary Search (Recursive): Divide and conquer on sorted array.
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion
    
    Args:
        arr: Sorted list to search in
        target: Element to find
        left: Left boundary
        right: Right boundary
    
    Returns:
        Index of element or -1 if not found
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def jump_search(arr, target):
    """
    Jump Search: Jump ahead by fixed steps, then linear search.
    
    Time Complexity: O(√n)
    Space Complexity: O(1)
    
    Args:
        arr: Sorted list to search in
        target: Element to find
    
    Returns:
        Index of element or -1 if not found
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Jump to find the block where element might be present
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search in the identified block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1


def interpolation_search(arr, target):
    """
    Interpolation Search: Improved binary search for uniformly distributed data.
    
    Time Complexity: O(log log n) average, O(n) worst
    Space Complexity: O(1)
    
    Args:
        arr: Sorted list with uniformly distributed values
        target: Element to find
    
    Returns:
        Index of element or -1 if not found
    """
    left, right = 0, len(arr) - 1
    
    while left <= right and arr[left] <= target <= arr[right]:
        # Avoid division by zero
        if arr[left] == arr[right]:
            if arr[left] == target:
                return left
            return -1
        
        # Estimate position using interpolation formula
        pos = left + int(((target - arr[left]) / (arr[right] - arr[left])) * (right - left))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1


def exponential_search(arr, target):
    """
    Exponential Search: Find range then apply binary search.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Args:
        arr: Sorted list to search in
        target: Element to find
    
    Returns:
        Index of element or -1 if not found
    """
    if not arr:
        return -1
    
    if arr[0] == target:
        return 0
    
    # Find range for binary search by repeated doubling
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    # Apply binary search on the found range
    left = i // 2
    right = min(i, len(arr) - 1)
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def find_first_occurrence(arr, target):
    """
    Find the first occurrence of target in sorted array with duplicates.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def find_last_occurrence(arr, target):
    """
    Find the last occurrence of target in sorted array with duplicates.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching in right half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# Example usage
if __name__ == "__main__":
    import time
    
    # Test with sorted array
    sorted_arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    target = 23
    
    print(f"Array: {sorted_arr}")
    print(f"Target: {target}\n")
    
    algorithms = {
        "Linear Search": lambda: linear_search(sorted_arr, target),
        "Binary Search (Iterative)": lambda: binary_search_iterative(sorted_arr, target),
        "Binary Search (Recursive)": lambda: binary_search_recursive(sorted_arr, target),
        "Jump Search": lambda: jump_search(sorted_arr, target),
        "Interpolation Search": lambda: interpolation_search(sorted_arr, target),
        "Exponential Search": lambda: exponential_search(sorted_arr, target),
    }
    
    for name, func in algorithms.items():
        start = time.perf_counter()
        result = func()
        end = time.perf_counter()
        print(f"{name:30}: Index {result} ({(end-start)*1000000:.2f} μs)")
    
    # Test with duplicates
    print("\n=== Testing with duplicates ===")
    dup_arr = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
    target_dup = 5
    print(f"Array: {dup_arr}")
    print(f"Target: {target_dup}")
    print(f"First occurrence: {find_first_occurrence(dup_arr, target_dup)}")
    print(f"Last occurrence: {find_last_occurrence(dup_arr, target_dup)}")
