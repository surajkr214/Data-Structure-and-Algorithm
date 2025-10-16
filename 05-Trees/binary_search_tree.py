"""
Binary Search Tree Implementation
A binary tree where left child < parent < right child.
"""


class TreeNode:
    """A node in the binary search tree."""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree with common operations."""
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        """
        Insert a new node into the BST.
        Time Complexity: O(log n) average, O(n) worst
        """
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """Helper method for recursive insertion."""
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
    
    def search(self, data):
        """
        Search for a value in the BST.
        Time Complexity: O(log n) average, O(n) worst
        """
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        """Helper method for recursive search."""
        if node is None:
            return False
        
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def delete(self, data):
        """
        Delete a node from the BST.
        Time Complexity: O(log n) average, O(n) worst
        """
        self.root = self._delete_recursive(self.root, data)
    
    def _delete_recursive(self, node, data):
        """Helper method for recursive deletion."""
        if node is None:
            return None
        
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node to be deleted found
            
            # Case 1: No children (leaf node)
            if node.left is None and node.right is None:
                return None
            
            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            # Case 3: Two children
            # Find inorder successor (smallest in right subtree)
            min_node = self._find_min(node.right)
            node.data = min_node.data
            node.right = self._delete_recursive(node.right, min_node.data)
        
        return node
    
    def _find_min(self, node):
        """Find the minimum value node in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def find_min_value(self):
        """Find the minimum value in the BST."""
        if self.root is None:
            return None
        node = self._find_min(self.root)
        return node.data
    
    def find_max_value(self):
        """Find the maximum value in the BST."""
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data
    
    def inorder_traversal(self):
        """
        Inorder traversal: Left, Root, Right
        Returns sorted elements for BST.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """
        Preorder traversal: Root, Left, Right
        Used for creating a copy of the tree.
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Helper method for preorder traversal."""
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """
        Postorder traversal: Left, Right, Root
        Used for deleting the tree.
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """Helper method for postorder traversal."""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)
    
    def level_order_traversal(self):
        """
        Level order traversal (BFS): Visit nodes level by level.
        """
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self):
        """Calculate the height of the tree."""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """Helper method for calculating height."""
        if node is None:
            return -1
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return 1 + max(left_height, right_height)
    
    def is_valid_bst(self):
        """Check if the tree is a valid BST."""
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_valid_bst_recursive(self, node, min_val, max_val):
        """Helper method for BST validation."""
        if node is None:
            return True
        
        if node.data <= min_val or node.data >= max_val:
            return False
        
        return (self._is_valid_bst_recursive(node.left, min_val, node.data) and
                self._is_valid_bst_recursive(node.right, node.data, max_val))


# Example usage
if __name__ == "__main__":
    # Create BST
    bst = BinarySearchTree()
    
    print("=== Building Binary Search Tree ===")
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
    print(f"Inserted values: {values}")
    
    # Traversals
    print("\n=== Tree Traversals ===")
    print(f"Inorder (sorted): {bst.inorder_traversal()}")
    print(f"Preorder: {bst.preorder_traversal()}")
    print(f"Postorder: {bst.postorder_traversal()}")
    print(f"Level order: {bst.level_order_traversal()}")
    
    # Search
    print("\n=== Search Operations ===")
    search_values = [40, 90]
    for val in search_values:
        found = bst.search(val)
        print(f"Search {val}: {'Found' if found else 'Not Found'}")
    
    # Min and Max
    print("\n=== Min and Max ===")
    print(f"Minimum value: {bst.find_min_value()}")
    print(f"Maximum value: {bst.find_max_value()}")
    
    # Height
    print(f"\nTree height: {bst.height()}")
    
    # Validation
    print(f"Is valid BST: {bst.is_valid_bst()}")
    
    # Delete
    print("\n=== Delete Operations ===")
    print(f"Deleting 20 (leaf node)")
    bst.delete(20)
    print(f"Inorder: {bst.inorder_traversal()}")
    
    print(f"Deleting 30 (node with two children)")
    bst.delete(30)
    print(f"Inorder: {bst.inorder_traversal()}")
    
    print(f"Deleting 50 (root node)")
    bst.delete(50)
    print(f"Inorder: {bst.inorder_traversal()}")
