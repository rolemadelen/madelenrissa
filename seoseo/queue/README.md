# Queue

- Implement using Linked List
  - [x] getFront()
  - [x] getRear()
  - [x] enqueue(value)
  - [x] dequeue()
- Implement using fixed-size array
  - [x] getFront()
  - [x] getRear()
  - [x] isEmpty()
  - [x] isFull()
  - [x] enqueue(value)
  - [x] dequeue()
- [x] What's the limitation of Queue implemented with a fixed-size array?
- [x] Know the time complexity for each methods

## Performance

- Size

  - Linked List : Can controll the size dynamically.
  - Fixed-size Array : The size is fixed, and you need to specify the size when creating the queue.

- Insert & Delete

  - Linked List : Finding the specific position and changing the links between nodes result in an average time complexity of O(n).
  - Fixed-size Array : Insert or delete elements in O(1) time.

- Memory Usage

  - Linked List : Since the array's size is fixed, even if the number of elements in the queue is less than the array's size, the array's size remains unchanged, leading to memory waste.
  - Fixed-size Array : It is more memory-efficient, becuase the size dynamically adjusts based on the number of elements.

- Overflow & Underflow

  - Linked List : Attempting to add elements beyond the queue's size causes overflow. Also, trying to remove elements from an empty queue results in underflow.
  - Fixed-size Array : Due to dynamic resizing, adding elements beyond the queue's size or removing elements from an empty queue is possible.

- Concurrency
  - Linked List : The fixed size may cause synchronization issues when multiple threads access the queue simultaneously.
  - Fixed-size Array : Since the size dynamically adjusts, there are no synchronization issues during queue access.

### Implement using Linked List

![queueCompare](https://github.com/rolemadelen/madelenrissa/assets/102719063/98248599-f792-4434-a7dd-97869b79682d)

### Implement using Fixed-size Array

![fixedFullandEmpty](https://github.com/rolemadelen/madelenrissa/assets/102719063/a390e696-e186-4df1-b60c-d672369a59dd)

## What's the limitation of a Queue implemented with a fixed-size array?

- Obviously, the size of the queue is fixed, so the programmer has to decide the size of the queue, and because of this, it could waste memory and sometimes lead to overflow or underflow.
- Also, as the queue's size remains unchanged during access, multiple threads accessing the queue simultaneously can lead to synchronization issues.
- Moreover,when attempting to add elements beyond the queue's size, the queue needs to be restructured. If the size of the queue is significantly large, the process for restructuring may take considerable time, leading to performance degradation.
- Because of these limitations of a Queue, implementing a queue with a fixed-size array may not be suitable for dynamically changing the size of the queue or for situations where the number of elements frequently changes.
