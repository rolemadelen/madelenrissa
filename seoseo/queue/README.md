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

### Implement using Linked List

![queueCompare](https://github.com/rolemadelen/madelenrissa/assets/102719063/98248599-f792-4434-a7dd-97869b79682d)

### Implement using Fixed-size Array

![fixedFullandEmpty](https://github.com/rolemadelen/madelenrissa/assets/102719063/a390e696-e186-4df1-b60c-d672369a59dd)

## What's the limitation of a Queue implemented with a fixed-size array?

- Obviously, the size of the queue is fixed, so the programmer has to decide the size of the queue, and because of this, it could waste memory and sometimes lead to overflow or underflow.
- Also, as the queue's size remains unchanged during access, multiple threads accessing the queue simultaneously can lead to synchronization issues.
- Moreover,when attempting to add elements beyond the queue's size, the queue needs to be restructured. If the size of the queue is significantly large, the process for restructuring may take considerable time, leading to performance degradation.
- Because of these limitations of a Queue, implementing a queue with a fixed-size array may not be suitable for dynamically changing the size of the queue or for situations where the number of elements frequently changes.
