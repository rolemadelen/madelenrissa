# Singly Linked List

- Implement
- [x] without tail pointer
- [x] with tail pointer
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
- [x] Know the time complexity for each methods
- [x] Know the difference between Singly, Doubly and Circular Linked List
  - Singly -> linear
  - Doubly -> a node with 2 pointers: next and previous nodes. It consumes relatively more memory than a Singly linked list because of extra pointer. But it's easier to traverse through the list.
  - Circular -> can be either Singly or Doubly. Last node links back to the first node and vice versa.
- [x] Know when to use Linked Lists and Arrays
  - Linked List -> linear access time, but its insert and delete operations are performed in constant time.
  - Array -> allows for constant time access to elements, but inserting and deleting elements in between can be expensive due to shifting of elements.

## Perforamnce

When performing 100,000 `pushBack` and `popBack` operations, the average execution time
was approximately 20 seconds for the linked list without a tail pointer. In contrast,
the linked list with a tail pointer achieved an execution time of around 10 seconds.

With a tail pointer:
![performance with tail](./bin/linked-list-with-tail.png)

Without the tail pointer:
![performance without tail](./bin/linked-list-without-tail.png)

## Problems

Linked list related problems selected from [Leetcode](https://leetcode.com/tag/linked-list/).

|       #       | Problem                                           | Difficulty |
| :-----------: | :------------------------------------------------ | :--------- |
|    [2][i2]    | Add Two Numbers                                   | Medium     |
|   [19][i19]   | Remove Nth Node From End of List                  | Medium     |
|   [21][i21]   | Merge Two Sorted Lists                            | Easy       |
|   [23][i23]   | Merge k Sorted Lists                              | Hard       |
|   [83][i83]   | Remove Duplicates from Sorted List                | Easy       |
|  [141][i141]  | Linked List Cycle                                 | Easy       |
|  [146][i146]  | LRU Cache                                         | Medium     |
|  [160][i160]  | Intersection of Two Linked Lists                  | Easy       |
|  [203][i203]  | Remove Linked List Elements                       | Easy       |
|  [206][i206]  | Reverse Linked List                               | Easy       |
|  [234][i234]  | Palindrome Linked List                            | Easy       |
|  [237][i237]  | Delete Node in a Linked List                      | Easy       |
|  [432][i432]  | All O`one Data Structure                          | Hard       |
|  [876][i876]  | Middle of the Linked List                         | Easy       |
| [1206][i1206] | Convert Binary Number in a Linked List to Integer | Easy       |
| [1290][i1290] | Design Skiplist                                   | Hard       |
| [1669][i1669] | Merge In Between Linked Lists                     | Medium     |
| [2181][i2181] | Merge Nodes in Between Zeros                      | Medium     |

[i2]: https://leetcode.com/problems/add-two-numbers/
[i19]: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
[i21]: https://leetcode.com/problems/merge-two-sorted-lists/
[i23]: https://leetcode.com/problems/merge-k-sorted-lists/
[i83]: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
[i141]: https://leetcode.com/problems/linked-list-cycle/
[i146]: https://leetcode.com/problems/lru-cache/
[i160]: https://leetcode.com/problems/intersection-of-two-linked-lists/
[i203]: https://leetcode.com/problems/remove-linked-list-elements/
[i206]: https://leetcode.com/problems/reverse-linked-list/
[i234]: https://leetcode.com/problems/palindrome-linked-list/
[i237]: https://leetcode.com/problems/delete-node-in-a-linked-list/
[i432]: https://leetcode.com/problems/all-oone-data-structure/
[i876]: https://leetcode.com/problems/middle-of-the-linked-list/
[i1206]: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
[i1290]: https://leetcode.com/problems/design-skiplist/
[i1669]: https://leetcode.com/problems/merge-in-between-linked-lists/
[i2181]: https://leetcode.com/problems/merge-nodes-in-between-zeros/
