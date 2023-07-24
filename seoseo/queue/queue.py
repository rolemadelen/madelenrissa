import time

start = time.time()  # save start time


def printTime(start):
    # current time - start time = runtime
    print("runtime :", time.time() - start)

# Start : Code

# class for Node without the No Tail


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None  # Pointing the first of the queue
        self.rear = None  # Pointing the last of the queue

    def isEmpty(self):
        return self.front is None

    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.isEmpty():
            return None
        # print("dequeue self.front.value - "+str(self.front.value))
        value = self.front.value
        # print("dequeue self.front.next.value - "+str(self.front.next.value))
        self.front = self.front.next
        return value

    def getFront(self):
        if self.isEmpty():
            return None
        return self.front.value

    def getRear(self):
        if self.isEmpty():
            return None
        return self.rear.value


# Queue implement test
if __name__ == "__main__":
    # print("Queue :", Queue)

    queue = Queue()
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

    # print("After Dequeue queue :", queue)


# End : Code
printTime(start)
