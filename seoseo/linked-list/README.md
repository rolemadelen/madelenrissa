# Singly Linked List
- What is?
  - A singly linked list is a type of data structure that consists of a sequence of nodes.
    Each node is a basic building block or unit of data that stores a value (or payload) and contains a reference (or link) to the next node in the sequence.
    Simply, a node is a data block or unit that holds data and points to the next node.
  - As a singly linked list, the pointer only stores the address value of the next node, making operations such as going back to the previous node impossible.
  

## Implement
  - [x] size()
  - [x] isEmpty()
  - [x] pushFront(value)
  - [x] pushBack(value)
  - [x] popFront()
  - [x] popBack()
  - [x] getFront()
  - [x] getBack()
  - [x] reverse()
  - [x] insert(index, value) - 0-based index
  - [x] without tail pointer
  - [ ] with tail pointer
  - [x] Know the time complexity for each method
  - [x] Know the difference between Singly, Doubly, and Circular Linked List
    - Singly -> linear
    - Doubly -> a node with 2 pointers: next and previous nodes. It consumes relatively more memory than a Singly linked list because of the extra pointer. But it's easier to traverse through the list.
    - Circular -> can be either Singly or Doubly. The last node links back to the first node and vice versa.
  - [ ] Know when to use Linked Lists and Arrays
    - Linked List -> linear access time, but its insert and delete operations are performed in O(1) constant time.
      - Linear Time : Searching, Insert/Delete an element in the middle of the Linked List(for searching), When the Linked List doesn't have a pointer & Insert/Delete an element in the end of the Linked List
      - Constant Time : When the Linked List has a pointer & Insert/Delete an element in the end of the Linked List, Insert/Delete an element in the first of the Linked List
    - Array -> allows for constant time access to elements, but inserting and deleting elements in between can be expensive due to the shifting of elements. Array can get the value in constant time if it has the index. If it does not have the index, than O(N) as linear time.
      - Linear time : Insert or delete an element in the array, when the position is the first or in the middle of the Array
      - Constant time : Insert or delete an element in the array at the end of the Array.

---

## Perforamnce
- Without Tail
<img width="840" alt="noTail" src="https://github.com/rolemadelen/madelenrissa/assets/102719063/b10e5e43-6365-462e-a31b-857a43aa6d10">

- With Tail


---
## Issue / Question

