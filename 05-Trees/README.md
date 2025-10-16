# Trees

## Overview
A tree is a hierarchical data structure with a root node and children nodes forming a parent-child relationship.

## Key Terms
- **Root**: Top node with no parent
- **Parent**: Node with children
- **Child**: Node with a parent
- **Leaf**: Node with no children
- **Height**: Length of longest path from node to leaf
- **Depth**: Length of path from root to node

## Types of Trees
1. **Binary Tree**: Each node has at most 2 children
2. **Binary Search Tree (BST)**: Left child < parent < right child
3. **AVL Tree**: Self-balancing BST
4. **Red-Black Tree**: Self-balancing BST
5. **B-Tree**: Self-balancing tree for databases

## Tree Traversals
1. **Inorder (Left, Root, Right)**: Gives sorted order for BST
2. **Preorder (Root, Left, Right)**: Used for copying tree
3. **Postorder (Left, Right, Root)**: Used for deleting tree
4. **Level Order**: Breadth-first traversal

## Time Complexity (BST)
- Search: O(log n) average, O(n) worst
- Insert: O(log n) average, O(n) worst
- Delete: O(log n) average, O(n) worst

## Files in this directory
- `binary_tree.py`: Binary tree implementation
- `binary_search_tree.py`: BST implementation with operations
