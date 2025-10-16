"""
Hash Table Implementation
Demonstrates hash table using chaining for collision resolution.
"""


class HashNode:
    """Node for storing key-value pairs in hash table."""
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """Hash table implementation using chaining."""
    
    def __init__(self, capacity=10):
        """
        Initialize hash table with given capacity.
        
        Args:
            capacity: Initial size of hash table
        """
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * capacity
    
    def _hash(self, key):
        """
        Hash function to compute index for a key.
        Uses Python's built-in hash() and modulo.
        
        Time Complexity: O(1)
        """
        return hash(key) % self.capacity
    
    def put(self, key, value):
        """
        Insert or update a key-value pair.
        
        Args:
            key: Key to insert/update
            value: Value to associate with key
        
        Time Complexity: O(1) average, O(n) worst case
        """
        index = self._hash(key)
        node = self.buckets[index]
        
        # Check if key already exists and update
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
        
        # Insert new node at beginning of chain
        new_node = HashNode(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self.size += 1
        
        # Resize if load factor exceeds threshold
        if self.size / self.capacity > 0.75:
            self._resize()
    
    def get(self, key):
        """
        Get value associated with key.
        
        Args:
            key: Key to look up
        
        Returns:
            Value associated with key, or None if not found
        
        Time Complexity: O(1) average, O(n) worst case
        """
        index = self._hash(key)
        node = self.buckets[index]
        
        while node:
            if node.key == key:
                return node.value
            node = node.next
        
        return None
    
    def remove(self, key):
        """
        Remove a key-value pair.
        
        Args:
            key: Key to remove
        
        Returns:
            True if removed, False if key not found
        
        Time Complexity: O(1) average, O(n) worst case
        """
        index = self._hash(key)
        node = self.buckets[index]
        prev = None
        
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[index] = node.next
                self.size -= 1
                return True
            prev = node
            node = node.next
        
        return False
    
    def contains(self, key):
        """
        Check if key exists in hash table.
        
        Args:
            key: Key to check
        
        Returns:
            True if key exists, False otherwise
        
        Time Complexity: O(1) average, O(n) worst case
        """
        index = self._hash(key)
        node = self.buckets[index]
        
        while node:
            if node.key == key:
                return True
            node = node.next
        
        return False
    
    def keys(self):
        """
        Get all keys in hash table.
        
        Returns:
            List of all keys
        
        Time Complexity: O(n)
        """
        all_keys = []
        for bucket in self.buckets:
            node = bucket
            while node:
                all_keys.append(node.key)
                node = node.next
        return all_keys
    
    def values(self):
        """
        Get all values in hash table.
        
        Returns:
            List of all values
        
        Time Complexity: O(n)
        """
        all_values = []
        for bucket in self.buckets:
            node = bucket
            while node:
                all_values.append(node.value)
                node = node.next
        return all_values
    
    def items(self):
        """
        Get all key-value pairs.
        
        Returns:
            List of (key, value) tuples
        
        Time Complexity: O(n)
        """
        all_items = []
        for bucket in self.buckets:
            node = bucket
            while node:
                all_items.append((node.key, node.value))
                node = node.next
        return all_items
    
    def _resize(self):
        """
        Resize hash table when load factor is too high.
        Doubles the capacity and rehashes all entries.
        
        Time Complexity: O(n)
        """
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0
        
        # Rehash all entries
        for bucket in old_buckets:
            node = bucket
            while node:
                self.put(node.key, node.value)
                node = node.next
    
    def get_load_factor(self):
        """Get current load factor."""
        return self.size / self.capacity
    
    def display(self):
        """Display hash table contents."""
        print(f"Hash Table (Size: {self.size}, Capacity: {self.capacity}, Load Factor: {self.get_load_factor():.2f})")
        for i, bucket in enumerate(self.buckets):
            if bucket:
                items = []
                node = bucket
                while node:
                    items.append(f"{node.key}:{node.value}")
                    node = node.next
                print(f"  Bucket {i}: {' -> '.join(items)}")


def count_frequency(arr):
    """
    Count frequency of elements using hash table.
    
    Args:
        arr: List of elements
    
    Returns:
        Dictionary with element frequencies
    """
    freq = HashTable()
    for item in arr:
        count = freq.get(item)
        freq.put(item, (count or 0) + 1)
    return dict(freq.items())


def find_duplicates(arr):
    """
    Find duplicate elements using hash table.
    
    Args:
        arr: List of elements
    
    Returns:
        List of duplicate elements
    
    Time Complexity: O(n)
    """
    seen = HashTable()
    duplicates_set = set()  # Use set for O(1) lookup
    
    for item in arr:
        if seen.contains(item):
            duplicates_set.add(item)
        else:
            seen.put(item, True)
    
    return list(duplicates_set)


def two_sum(arr, target):
    """
    Find two numbers that add up to target.
    
    Args:
        arr: List of numbers
        target: Target sum
    
    Returns:
        Tuple of indices (i, j) or None if not found
    
    Time Complexity: O(n)
    """
    seen = HashTable()
    
    for i, num in enumerate(arr):
        complement = target - num
        if seen.contains(complement):
            return (seen.get(complement), i)
        seen.put(num, i)
    
    return None


# Example usage
if __name__ == "__main__":
    print("=== Basic Hash Table Operations ===")
    ht = HashTable(capacity=5)
    
    # Insert key-value pairs
    ht.put("name", "Alice")
    ht.put("age", 25)
    ht.put("city", "London")
    ht.put("country", "UK")
    
    ht.display()
    
    # Get values
    print(f"\nName: {ht.get('name')}")
    print(f"Age: {ht.get('age')}")
    print(f"Job: {ht.get('job')}")  # Not exists
    
    # Update value
    print("\nUpdating age to 26...")
    ht.put("age", 26)
    print(f"Age: {ht.get('age')}")
    
    # Check existence
    print(f"\nContains 'city': {ht.contains('city')}")
    print(f"Contains 'job': {ht.contains('job')}")
    
    # Get all keys and values
    print(f"\nAll keys: {ht.keys()}")
    print(f"All values: {ht.values()}")
    
    # Remove entry
    print("\nRemoving 'city'...")
    ht.remove("city")
    ht.display()
    
    # Count frequency
    print("\n=== Frequency Counter ===")
    numbers = [1, 2, 3, 2, 1, 4, 5, 4, 1]
    freq = count_frequency(numbers)
    print(f"Array: {numbers}")
    print(f"Frequency: {freq}")
    
    # Find duplicates
    print("\n=== Find Duplicates ===")
    arr = [1, 2, 3, 4, 2, 5, 6, 3]
    duplicates = find_duplicates(arr)
    print(f"Array: {arr}")
    print(f"Duplicates: {duplicates}")
    
    # Two Sum problem
    print("\n=== Two Sum Problem ===")
    numbers = [2, 7, 11, 15]
    target = 9
    result = two_sum(numbers, target)
    print(f"Array: {numbers}")
    print(f"Target: {target}")
    if result:
        print(f"Indices: {result}, Values: [{numbers[result[0]]}, {numbers[result[1]]}]")
    else:
        print("No solution found")
