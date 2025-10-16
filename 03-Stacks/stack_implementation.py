"""
Stack Implementation
Demonstrates LIFO (Last In First Out) data structure.
"""


class Stack:
    """Stack implementation using Python list."""
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        Time Complexity: O(1)
        """
        self.items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """
        Return the top item without removing it.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
    
    def display(self):
        """Display the stack contents."""
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack (top to bottom):", self.items[::-1])


def is_balanced_parentheses(expression):
    """
    Check if parentheses in an expression are balanced.
    
    Args:
        expression: String containing parentheses
    
    Returns:
        True if balanced, False otherwise
    """
    stack = Stack()
    opening = "([{"
    closing = ")]}"
    pairs = {"(": ")", "[": "]", "{": "}"}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()


def reverse_string(text):
    """
    Reverse a string using a stack.
    
    Args:
        text: String to reverse
    
    Returns:
        Reversed string
    """
    stack = Stack()
    
    # Push all characters onto the stack
    for char in text:
        stack.push(char)
    
    # Pop all characters to build reversed string
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    
    return reversed_text


def evaluate_postfix(expression):
    """
    Evaluate a postfix expression.
    
    Args:
        expression: String in postfix notation (space-separated)
        Example: "3 4 + 2 *" = (3 + 4) * 2 = 14
    
    Returns:
        Result of the expression
    """
    stack = Stack()
    operators = {'+', '-', '*', '/'}
    
    tokens = expression.split()
    
    for token in tokens:
        if token not in operators:
            # It's a number
            stack.push(float(token))
        else:
            # It's an operator
            if stack.size() < 2:
                raise ValueError("Invalid postfix expression")
            
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            
            stack.push(result)
    
    if stack.size() != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack.pop()


# Example usage
if __name__ == "__main__":
    # Basic stack operations
    print("=== Basic Stack Operations ===")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    
    print(f"Top element: {stack.peek()}")
    print(f"Popped: {stack.pop()}")
    stack.display()
    print(f"Size: {stack.size()}")
    
    # Balanced parentheses
    print("\n=== Balanced Parentheses Check ===")
    expressions = ["(())", "({[]})", "(()", "({[})]"]
    for expr in expressions:
        result = is_balanced_parentheses(expr)
        print(f"{expr}: {'Balanced' if result else 'Not Balanced'}")
    
    # Reverse string
    print("\n=== String Reversal ===")
    text = "Hello World"
    print(f"Original: {text}")
    print(f"Reversed: {reverse_string(text)}")
    
    # Evaluate postfix
    print("\n=== Postfix Evaluation ===")
    postfix_expr = "3 4 + 2 *"
    print(f"Expression: {postfix_expr}")
    print(f"Result: {evaluate_postfix(postfix_expr)}")
