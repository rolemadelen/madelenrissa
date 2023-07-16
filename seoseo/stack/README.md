# Stack


## Implement using Linked List
- [x] top()
- [x] isEmpty()
- [x] push(value)
- [x] pop()
- [x] Know the time complexity for each methods

### Stack
- A stack is a fundamental data structure that follows the Last-In-First-Out (LIFO) principle.
- The Last-In-First-Out principle states that the element which is inserted last is the first one to be removed.
- The stack operates on a specific end called the "top" of the stack.
- **Top**: The top of the stack refers to the position where the most recently added element is located.

- The implementation of the stack using a linked list does not require a tail pointer because the stack operations such as push and pop are performed on the top of the stack, so we only need to keep track of the topmost node.


---

## Perforamnce
- Stack with linked-list
<img width="247" alt="screenshot_stack" src="https://github.com/rolemadelen/madelenrissa/assets/102719063/1dbfe04a-7ea5-4ae5-bfec-14e0c6358013">

- Stack with array == list ps python
<img width="240" alt="screenshot_stack_array" src="https://github.com/rolemadelen/madelenrissa/assets/102719063/365c71cc-1087-471e-8508-a8d53567b965">


---
## Issue / Question

### Difference of liked-list and array to implement

- In terms of space complexity, implementing a stack using a Python list does not require additional memory space. The list itself allocates memory to store the elements.
- In contrast, implementing a stack using a linked list requires allocating memory for each node bacase the node is class.
- Therefore, the memory usage can increase based on the number of elements.

- Also the **"Time Complexity"** is O(1). Because append(), pop() and top() method accessing the last element in the list that takes O(1) time.

- In a stack implementation using a linked list, the push(), pop(), and top() operations all execute in O(1) time. This is because adding a new node at the front, removing or returning the first node, and accessing the value of the first node are all fast operations.