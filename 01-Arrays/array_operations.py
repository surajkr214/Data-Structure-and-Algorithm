"""
Basic Array Operations
This module demonstrates fundamental operations on arrays/lists.
"""


def insert_element(arr, element, position=None):
    """
    Insert an element into the array.
    
    Args:
        arr: The list to insert into
        element: The element to insert
        position: Position to insert at (None for end)
    
    Returns:
        The modified list
    """
    if position is None:
        arr.append(element)
    else:
        arr.insert(position, element)
    return arr


def delete_element(arr, position):
    """
    Delete an element from the array at given position.
    
    Args:
        arr: The list to delete from
        position: Index of element to delete
    
    Returns:
        The deleted element
    """
    if 0 <= position < len(arr):
        return arr.pop(position)
    return None


def search_element(arr, element):
    """
    Search for an element in the array.
    
    Args:
        arr: The list to search in
        element: The element to find
    
    Returns:
        Index of element or -1 if not found
    """
    try:
        return arr.index(element)
    except ValueError:
        return -1


def reverse_array(arr):
    """
    Reverse the array in-place.
    
    Args:
        arr: The list to reverse
    
    Returns:
        The reversed list
    """
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def find_maximum(arr):
    """
    Find the maximum element in the array.
    
    Args:
        arr: The list to search
    
    Returns:
        Maximum element or None if empty
    """
    if not arr:
        return None
    return max(arr)


def find_minimum(arr):
    """
    Find the minimum element in the array.
    
    Args:
        arr: The list to search
    
    Returns:
        Minimum element or None if empty
    """
    if not arr:
        return None
    return min(arr)


# Example usage
if __name__ == "__main__":
    # Create an array
    numbers = [10, 20, 30, 40, 50]
    print(f"Original array: {numbers}")
    
    # Insert element
    insert_element(numbers, 25, 2)
    print(f"After inserting 25 at position 2: {numbers}")
    
    # Search element
    index = search_element(numbers, 30)
    print(f"Element 30 found at index: {index}")
    
    # Delete element
    deleted = delete_element(numbers, 2)
    print(f"Deleted element: {deleted}, Array: {numbers}")
    
    # Reverse array
    reverse_array(numbers)
    print(f"Reversed array: {numbers}")
    
    # Find max and min
    print(f"Maximum: {find_maximum(numbers)}")
    print(f"Minimum: {find_minimum(numbers)}")
