import time

start = time.time()  # save start time


def printTime(start):
    # current time - start time = runtime
    print("runtime :", time.time() - start)

# Start : Code


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity  # 큐의 최대 크기
        self.queue = [None] * capacity  # 큐를 나타내는 배열
        self.front = 0  # Pointer for the first of the queue
        self.rear = 0   # Pointer for the last of the queue
        self.size = 0   # number of elements in the queue

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.isFull():  # check for capacity
            print("The queue full!")
            return

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.isEmpty():  # check for its availablity to deque
            print("The queue is empty!")
            return None

        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def getFront(self):
        if self.isEmpty():
            return None
        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            return None
        return self.queue[self.rear - 1]


# Queue implement test
if __name__ == "__main__":
    # print("Queue :", Queue)

    queue = Queue(3)  # fixed size
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)

    # print("queue :", queue)

    print("Front:", queue.getFront())
    print("Rear:", queue.getRear())

    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())

    # print("After Dequeue queue :", queue)


# End : Code
printTime(start)
