# Contributing Guidelines

Thank you for considering contributing to this Data Structures and Algorithms repository! This guide will help you get started.

## 🎯 How Can You Contribute?

### 1. Add New Implementations
- Implement missing data structures or algorithms
- Add variations of existing implementations
- Include time and space complexity analysis

### 2. Improve Documentation
- Add better explanations
- Include visual diagrams
- Fix typos and formatting
- Add more examples

### 3. Add Test Cases
- Write unit tests for implementations
- Add edge case testing
- Include performance benchmarks

### 4. Fix Bugs
- Report bugs via Issues
- Submit fixes with clear explanation
- Include test cases for the fix

### 5. Optimize Code
- Improve efficiency
- Reduce space complexity
- Make code more readable

## 📋 Submission Guidelines

### Code Style
- Use clear, descriptive variable names
- Add docstrings to all functions and classes
- Include complexity analysis in comments
- Follow PEP 8 style guide for Python code

### Documentation Format
```python
def function_name(parameters):
    """
    Brief description of what the function does.
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    
    Args:
        param1: Description of parameter
        param2: Description of parameter
    
    Returns:
        Description of return value
    
    Example:
        >>> function_name(example_input)
        expected_output
    """
    # Implementation
    pass
```

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove, etc.)
- Examples:
  - "Add heap sort implementation"
  - "Fix bug in binary search edge case"
  - "Update README with graph algorithms"

### Pull Request Process

1. **Fork the Repository**
   ```bash
   # Click 'Fork' button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Data-Structure-and-Algorithm.git
   cd Data-Structure-and-Algorithm
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**
   - Write clean, well-documented code
   - Test your implementation
   - Add examples if applicable

5. **Test Your Code**
   ```bash
   # Run your implementation
   python your_module.py
   
   # Ensure no errors
   ```

6. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add descriptive commit message"
   ```

7. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill in the PR template
   - Submit for review

### Pull Request Template

```markdown
## Description
Brief description of your changes

## Type of Change
- [ ] New implementation
- [ ] Bug fix
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please describe)

## Checklist
- [ ] Code follows style guidelines
- [ ] Added/updated documentation
- [ ] Tested implementation
- [ ] Added complexity analysis
- [ ] Added examples

## Testing
Describe how you tested your changes
```

## 📝 Directory Structure

When adding new content, follow this structure:

```
XX-TopicName/
├── README.md              # Overview and explanation
├── implementation.py      # Main implementation
└── examples.py           # Additional examples (optional)
```

## 🎓 Educational Focus

Remember, this is an educational repository. When contributing:

- **Clarity over Cleverness**: Write code that's easy to understand
- **Explain Concepts**: Add comments explaining the "why"
- **Show Examples**: Include practical use cases
- **Be Beginner-Friendly**: Assume readers are learning

## ❓ Questions or Suggestions?

- Open an Issue for discussion
- Ask questions in Pull Request comments
- Suggest improvements via Issues

## 🙏 Thank You!

Your contributions help students learn and grow. Every improvement, no matter how small, is valuable!

---

**Happy Contributing! 🚀**
