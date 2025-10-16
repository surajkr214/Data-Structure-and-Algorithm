# Linked Lists

## Overview
A linked list is a linear data structure where elements are stored in nodes. Each node contains data and a reference (link) to the next node.

## Types
1. **Singly Linked List**: Each node points to the next node
2. **Doubly Linked List**: Each node points to both next and previous nodes
3. **Circular Linked List**: Last node points back to the first node

## Time Complexity
- Access: O(n)
- Search: O(n)
- Insertion: O(1) at head, O(n) at specific position
- Deletion: O(1) at head, O(n) at specific position

## Advantages over Arrays
- Dynamic size
- Efficient insertion/deletion at beginning
- No memory wastage

## Disadvantages
- No random access
- Extra memory for pointers
- Not cache-friendly

## Files in this directory
- `singly_linked_list.py`: Singly linked list implementation
- `doubly_linked_list.py`: Doubly linked list implementation
