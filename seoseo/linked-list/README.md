# Singly Linked List
- What is?
  - A singly linked list is a type of data structure that consists of a sequence of nodes.
    Each node is a basic building block or unit of data that stores a value (or payload) and contains a reference (or link) to the next node in the sequence.
    Simply, a node is a data block or unit that holds data and points to the next node.
  - As a singly linked list, the pointer only stores the address value of the next node, making operations such as going back to the previous node impossible.
  

## Implement
  - [ ] size()
  - [ ] isEmpty()
  - [ ] pushFront(value)
  - [ ] pushBack(value)
  - [ ] popFront()
  - [ ] popBack()
  - [ ] getFront()
  - [ ] getBack()
  - [ ] reverse()
  - [ ] insert(index, value) - 0-based index
  - [ ] without tail pointer
  - [ ] with tail pointer
  - [ ] Know the time complexity for each method
  - [ ] Know the difference between Singly, Doubly, and Circular Linked List
    - Singly -> linear
    - Doubly -> a node with 2 pointers: next and previous nodes. It consumes relatively more memory than a Singly linked list because of the extra pointer. But it's easier to traverse through the list.
    - Circular -> can be either Singly or Doubly. The last node links back to the first node and vice versa.
  - [ ] Know when to use Linked Lists and Arrays
    - Linked List -> linear access time, but its insert and delete operations are performed in constant time.
    - Array -> allows for constant time access to elements, but inserting and deleting elements in between can be expensive due to the shifting of elements.

---

## Perforamnce




