# Data Structures & Algorithms - Quick Reference

## 🚀 Time Complexity Cheat Sheet

### Data Structures

| Data Structure | Access | Search | Insert | Delete | Space |
|---------------|--------|--------|--------|--------|-------|
| **Array** | O(1) | O(n) | O(n) | O(n) | O(n) |
| **Linked List** | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| **Stack** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Queue** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Hash Table** | N/A | O(1)** | O(1)** | O(1)** | O(n) |
| **Binary Search Tree** | O(log n)** | O(log n)** | O(log n)** | O(log n)** | O(n) |
| **AVL Tree** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **Binary Heap** | N/A | O(n) | O(log n) | O(log n) | O(n) |

\* At head/tail position only  
** Average case; worst case can be O(n)

### Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| **Counting Sort** | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n+k) | Yes |

### Searching Algorithms

| Algorithm | Time Complexity | Space | Requirements |
|-----------|----------------|-------|--------------|
| **Linear Search** | O(n) | O(1) | None |
| **Binary Search** | O(log n) | O(1) | Sorted array |
| **Jump Search** | O(√n) | O(1) | Sorted array |
| **Interpolation Search** | O(log log n) avg, O(n) worst | O(1) | Sorted, uniform distribution |
| **Exponential Search** | O(log n) | O(1) | Sorted array |

## 📊 When to Use What?

### Choosing a Data Structure

**Use Array/List when:**
- Need random access by index
- Size is known or doesn't change much
- Memory locality is important
- Simple implementation needed

**Use Linked List when:**
- Frequent insertions/deletions at beginning
- Size changes frequently
- No need for random access
- Memory is fragmented

**Use Stack when:**
- Need LIFO behavior
- Function calls, undo operations
- Expression evaluation
- Backtracking algorithms

**Use Queue when:**
- Need FIFO behavior
- Scheduling, buffering
- BFS traversal
- Resource sharing

**Use Hash Table when:**
- Need fast lookups (O(1))
- Implementing cache, dictionary
- Counting frequencies
- Detecting duplicates

**Use Binary Search Tree when:**
- Need sorted data
- Frequent search operations
- Dynamic dataset
- Range queries needed

**Use Heap when:**
- Need min/max quickly
- Priority queue implementation
- Finding k largest/smallest elements
- Median finding

**Use Graph when:**
- Representing networks
- Social connections
- Maps and navigation
- Dependencies

### Choosing a Sorting Algorithm

**Use Bubble Sort when:**
- Learning purposes only
- Data is nearly sorted
- Small datasets (< 10 elements)

**Use Insertion Sort when:**
- Small datasets (< 50 elements)
- Data is nearly sorted
- Online sorting (data arrives in real-time)

**Use Merge Sort when:**
- Need stable sort
- Need guaranteed O(n log n)
- Sorting linked lists
- External sorting (large files)

**Use Quick Sort when:**
- Average case performance matters
- Space is limited
- Good cache performance needed
- Most general-purpose sorting

**Use Heap Sort when:**
- Space is limited (O(1))
- Consistent performance needed
- No stability requirement

**Use Counting/Radix Sort when:**
- Sorting integers with known range
- Need linear time complexity
- Stability is important

### Choosing a Searching Algorithm

**Use Linear Search when:**
- Array is unsorted
- Small dataset
- Searching linked list

**Use Binary Search when:**
- Array is sorted
- Large dataset
- O(log n) performance needed

**Use Hash Table when:**
- Need O(1) average lookup
- Can afford extra space
- Unique keys

## 🎯 Common Patterns

### Two Pointers
```python
# Use when: Array problems, finding pairs, removing duplicates
left, right = 0, len(arr) - 1
while left < right:
    # Process
    if condition:
        left += 1
    else:
        right -= 1
```

### Sliding Window
```python
# Use when: Subarray/substring problems, fixed/variable window
window_start = 0
for window_end in range(len(arr)):
    # Add element to window
    while need_to_shrink:
        # Remove from window_start
        window_start += 1
```

### Fast & Slow Pointers
```python
# Use when: Cycle detection, finding middle, linked list problems
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### Recursion Pattern
```python
# Use when: Tree/graph traversal, divide and conquer
def recursive_function(params):
    # Base case
    if base_condition:
        return base_value
    
    # Recursive case
    return recursive_function(modified_params)
```

### Backtracking Pattern
```python
# Use when: Finding all solutions, permutations, combinations
def backtrack(state):
    if is_solution(state):
        add_to_results(state)
        return
    
    for choice in get_choices(state):
        make_choice(choice)
        backtrack(new_state)
        undo_choice(choice)
```

## 💡 Common Interview Tricks

1. **Hash Table for O(1) lookup**: Trade space for time
2. **Sort first**: Many problems become easier when sorted
3. **Two pointers**: Optimize nested loops
4. **Binary search**: Can be used beyond searching
5. **Stack for parentheses**: Match opening/closing
6. **Queue for BFS**: Level-order traversal
7. **Union-Find**: Connected components
8. **Trie for strings**: Prefix matching
9. **Dynamic Programming**: Overlapping subproblems
10. **Greedy**: Make locally optimal choice

## 🎓 Study Tips

1. **Understand time/space complexity first**
2. **Practice implementing from scratch**
3. **Draw diagrams for visualization**
4. **Test with edge cases** (empty, single element, duplicates)
5. **Explain your approach before coding**
6. **Start with brute force, then optimize**
7. **Use meaningful variable names**
8. **Write clean, readable code**

## 📚 Practice Problems by Topic

### Arrays
- Two Sum
- Best Time to Buy/Sell Stock
- Maximum Subarray
- Rotate Array
- Contains Duplicate

### Linked Lists
- Reverse Linked List
- Merge Two Sorted Lists
- Detect Cycle
- Remove Nth Node
- Intersection of Lists

### Stacks & Queues
- Valid Parentheses
- Min Stack
- Implement Queue using Stacks
- Daily Temperatures
- Sliding Window Maximum

### Trees
- Maximum Depth
- Same Tree
- Invert Binary Tree
- Path Sum
- Lowest Common Ancestor

### Sorting & Searching
- Binary Search
- Search in Rotated Array
- Find Peak Element
- Kth Largest Element
- Merge Intervals

---

**Remember**: Understanding > Memorization. Focus on concepts, not just solutions!
