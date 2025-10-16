# Data Structures and Algorithms

This repository contains comprehensive resources and implementations for the Data Structures and Algorithms module, taught at the University of East London for BSc. Hons Data Science and AI students.

## 📚 Contents

### 1. Arrays and Lists (`01-Arrays/`)
- Basic array operations (insertion, deletion, searching)
- Two-pointer techniques
- Sliding window algorithms
- **Time Complexity**: O(1) access, O(n) search
- [View Examples →](01-Arrays/)

### 2. Linked Lists (`02-LinkedLists/`)
- Singly Linked List implementation
- Doubly Linked List implementation
- Common operations and algorithms
- **Time Complexity**: O(n) access/search, O(1) insertion at head
- [View Examples →](02-LinkedLists/)

### 3. Stacks (`03-Stacks/`)
- LIFO (Last In First Out) principle
- Stack using lists and linked lists
- Applications: parentheses matching, expression evaluation, string reversal
- **Time Complexity**: O(1) for push, pop, peek
- [View Examples →](03-Stacks/)

### 4. Queues (`04-Queues/`)
- FIFO (First In First Out) principle
- Simple Queue and Circular Queue
- Applications: BFS, scheduling, buffering
- **Time Complexity**: O(1) for enqueue, dequeue
- [View Examples →](04-Queues/)

### 5. Trees (`05-Trees/`)
- Binary Tree concepts
- Binary Search Tree (BST) implementation
- Tree traversals: Inorder, Preorder, Postorder, Level-order
- **Time Complexity**: O(log n) average for BST operations
- [View Examples →](05-Trees/)

### 6. Sorting Algorithms (`06-Sorting/`)
Implementation and comparison of sorting algorithms:
- **Bubble Sort**: O(n²) - Simple but inefficient
- **Selection Sort**: O(n²) - Good for small datasets
- **Insertion Sort**: O(n²) - Efficient for nearly sorted data
- **Merge Sort**: O(n log n) - Divide and conquer
- **Quick Sort**: O(n log n) average - Very efficient in practice
- **Counting Sort**: O(n + k) - Non-comparison based
- [View Examples →](06-Sorting/)

### 7. Searching Algorithms (`07-Searching/`)
Implementation and comparison of searching algorithms:
- **Linear Search**: O(n) - Works on unsorted data
- **Binary Search**: O(log n) - Requires sorted data
- **Jump Search**: O(√n) - Better than linear
- **Interpolation Search**: O(log log n) - For uniform distribution
- **Exponential Search**: O(log n) - For unbounded arrays
- [View Examples →](07-Searching/)

### 8. Graphs (`08-Graphs/`)
- Graph representation (Adjacency List)
- BFS and DFS traversals
- Shortest path algorithms
- Cycle detection
- **Time Complexity**: O(V + E) for traversals
- [View Examples →](08-Graphs/)

### 9. Hashing (`09-Hashing/`)
- Hash table implementation with chaining
- Collision resolution techniques
- Common applications: frequency counter, duplicates, two sum
- **Time Complexity**: O(1) average for operations
- [View Examples →](09-Hashing/)

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Basic understanding of programming concepts

### Running the Examples

Each directory contains Python files with implementations and examples. To run any example:

```bash
# Navigate to the repository
cd Data-Structure-and-Algorithm

# Run any implementation file
python 01-Arrays/array_operations.py
python 02-LinkedLists/singly_linked_list.py
python 03-Stacks/stack_implementation.py
python 04-Queues/queue_implementation.py
python 05-Trees/binary_search_tree.py
python 06-Sorting/sorting_algorithms.py
python 07-Searching/searching_algorithms.py
```

## 📖 Learning Path

For beginners, we recommend following this order:

1. **Start with Arrays**: Fundamental data structure, easy to understand
2. **Move to Linked Lists**: Introduction to pointers and dynamic structures
3. **Learn Stacks and Queues**: Build on linked lists, understand LIFO and FIFO
4. **Study Trees**: Hierarchical structures, important for many algorithms
5. **Master Sorting**: Essential algorithms, various techniques
6. **Practice Searching**: Efficient data retrieval methods
7. **Explore Graphs**: Complex relationships and advanced algorithms
8. **Understand Hashing**: Fast lookups and data organization

## 🎯 Key Concepts

### Time Complexity (Big O Notation)
- **O(1)**: Constant time - Best performance
- **O(log n)**: Logarithmic time - Very efficient (e.g., binary search)
- **O(n)**: Linear time - Decent performance
- **O(n log n)**: Linearithmic time - Efficient sorting
- **O(n²)**: Quadratic time - Avoid for large datasets
- **O(2ⁿ)**: Exponential time - Very slow, avoid if possible

### Space Complexity
Consider memory usage alongside time complexity for complete analysis.

## 📝 Best Practices

1. **Understand the Problem**: Read carefully before coding
2. **Choose Right Data Structure**: Match structure to problem requirements
3. **Consider Trade-offs**: Time vs. space complexity
4. **Test Edge Cases**: Empty inputs, single elements, large datasets
5. **Write Clean Code**: Use meaningful names and comments
6. **Analyze Complexity**: Always know time and space complexity

## 🤝 Contributing

Contributions are welcome! If you'd like to add more examples, fix bugs, or improve documentation:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Test your code
5. Commit your changes (`git commit -am 'Add new feature'`)
6. Push to the branch (`git push origin feature/improvement`)
7. Create a Pull Request

## 📚 Additional Resources

- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- [VisuAlgo](https://visualgo.net/) - Visualize data structures and algorithms
- [GeeksforGeeks](https://www.geeksforgeeks.org/) - Tutorials and practice problems
- [LeetCode](https://leetcode.com/) - Coding practice platform

## 📄 License

This repository is for educational purposes. Feel free to use and modify the code for learning.

## 👨‍🎓 About

Created for BSc. Hons Data Science and AI students at the University of East London.

---

**Happy Learning! 🎓**
