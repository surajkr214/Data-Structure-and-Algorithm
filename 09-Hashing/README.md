# Hashing

## Overview
Hashing is a technique to map data of arbitrary size to fixed-size values. A hash function converts keys into array indices.

## Key Concepts
- **Hash Function**: Maps keys to indices
- **Hash Table**: Array that stores key-value pairs
- **Collision**: When two keys hash to same index
- **Load Factor**: n/m (items/table size)

## Hash Functions

### Good Hash Function Properties
1. **Deterministic**: Same input → same output
2. **Uniform Distribution**: Spreads keys evenly
3. **Fast Computation**: O(1) time
4. **Minimize Collisions**: Different keys → different indices

### Common Hash Functions
1. **Division Method**: h(k) = k mod m
2. **Multiplication Method**: h(k) = ⌊m(kA mod 1)⌋
3. **Universal Hashing**: Randomly select from family of functions

## Collision Resolution

### 1. Chaining (Open Hashing)
- Each bucket contains a linked list
- Store all colliding elements in list
- **Time**: O(1 + α) where α is load factor
- **Space**: O(n + m)
- **Advantage**: Simple, handles high load factors

### 2. Open Addressing (Closed Hashing)
All elements stored in the hash table itself.

**a) Linear Probing**
- h(k, i) = (h(k) + i) mod m
- Check next slot sequentially
- **Clustering**: Primary clustering problem

**b) Quadratic Probing**
- h(k, i) = (h(k) + c₁i + c₂i²) mod m
- Check slots in quadratic manner
- **Clustering**: Secondary clustering

**c) Double Hashing**
- h(k, i) = (h₁(k) + i·h₂(k)) mod m
- Use two hash functions
- **Best**: Minimal clustering

## Time Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| **Search** | O(1) | O(n) |
| **Insert** | O(1) | O(n) |
| **Delete** | O(1) | O(n) |

## Applications

1. **Databases**: Indexing records
2. **Caches**: Store frequently accessed data
3. **Sets**: Fast membership testing
4. **Dictionaries**: Key-value storage
5. **Symbol Tables**: Compilers
6. **Password Storage**: Secure hashing
7. **Cryptography**: Data integrity
8. **Load Balancing**: Consistent hashing

## Hash Table vs. Other Structures

| Feature | Hash Table | BST | Array |
|---------|-----------|-----|-------|
| **Search** | O(1) avg | O(log n) | O(n) |
| **Insert** | O(1) avg | O(log n) | O(n) |
| **Delete** | O(1) avg | O(log n) | O(n) |
| **Ordered** | No | Yes | No |
| **Memory** | High | Medium | Low |

## Common Problems

1. Two Sum
2. Group Anagrams
3. Longest Substring Without Repeating
4. Subarray Sum Equals K
5. Longest Consecutive Sequence

## Files in this directory
- `hash_table.py`: Hash table implementation with chaining
- `hash_applications.py`: Common hashing applications
