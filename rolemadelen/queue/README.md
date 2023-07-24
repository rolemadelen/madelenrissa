# Queue Array

Queue is a linear data structure that follows a particular order (First-In, First-Out) in which operations are performed.

<a href="https://www.programiz.com/dsa/queue"><img src="https://cdn.programiz.com/sites/tutorial2program/files/queue.png" title="programiz.com" alt="Queue" /></a>

In programming, the term **enqueue** refers to adding an item to the queue and **dequeue** for removing an item from the queue.

|      | enqueue | dequeue | empty | full |
| :--: | :-----: | :-----: | :---: | :--: |
| Time |  O(1)   |  O(1)   | O(1)  | O(1) |

## Pseudocode for Basic Operations

### enqueue

```text
push(queue<T>, front, rear, value) -> void
    Pre: queue is the queue array
         rear index tracks the most recently added element (last element in queue array)
         front index tracks the first element
         value is the value we're going to enqueue
    Post: new element is added to the queue

    queue[rear++] = value
END
```

### dequeue

```text
dequeue(queue<T>, front, rear) -> T
    Pre: queue is the queue array
         rear index tracks the most recently added element (last element in queue array)
         front index tracks the first element
    Post: front element has been removed from the queue

    elem = queue[front++];
    return elem
END
```

### empty

```text
empty(queue<T>, front, rear) -> boolean
    Pre: queue is the queue array
         rear index tracks the most recently added element (last element in queue array)
         front index tracks the first element
    Post: returns true if queue is empty; otherwise false;

    return front == rear
END
```

### full

```text
full(queue<T>, size, rear) -> boolean
    Pre: queue is the queue array
         size is the array size
         rear index tracks the most recently added element (last element in queue array)
    Post: returns true if queue is empty; otherwise false;

    return rear == size
END
```

## Problems

Queue related problems selected from [Leetcode](https://leetcode.com/tag/queue/).

|       #       | Problem                                | Difficulty |
| :-----------: | :------------------------------------- | :--------- |
|  [225][i225]  | Implement Stack using Queues           | Easy       |
|  [933][i933]  | Number of Recent Calls                 | Easy       |
| [1700][i1700] | Number of Students Unable to Eat Lunch | Easy       |
|  [950][i950]  | Reveal Cards In Increasing Order       | Medium     |
| [1670][i1670] | Design Front Middle Back Queue         | Medium     |
| [1823][i1823] | Find the Winner of the Circular Game   | Medium     |
| [2327][i2327] | Number of People Aware of a Secret     | Medium     |
|  [239][i239]  | Sliding Window Maximum                 | Hard       |
|  [936][i936]  | Stamping The Sequence                  | Hard       |
| [2444][i2444] | Count Subarrays With Fixed Bounds      | Hard       |

[i225]: https://leetcode.com/problems/implement-stack-using-queues/
[i933]: https://leetcode.com/problems/number-of-recent-calls/
[i1700]: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
[i950]: https://leetcode.com/problems/reveal-cards-in-increasing-order/
[i1670]: https://leetcode.com/problems/design-front-middle-back-queue/
[i1823]: https://leetcode.com/problems/find-the-winner-of-the-circular-game/
[i2327]: https://leetcode.com/problems/number-of-people-aware-of-a-secret/
[i239]: https://leetcode.com/problems/sliding-window-maximum/
[i936]: https://leetcode.com/problems/stamping-the-sequence/
[i2444]: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
