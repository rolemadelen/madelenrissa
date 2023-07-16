import time

start = time.time()  # save start time
def printTime(start):
    print("runtime :", time.time() - start)  # current time - start time = runtime


# Start : Code

# class for Node without the Tail
class Node :
    def __init__(self, value = 0, next=None) -> None:
        self.value = value
        self.next = next

# class : Stack
class Stack : 
    def __init__ (self) : 
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def push(self, value): 
        node = Node(value)
        if self.isEmpty() :
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def pop(self):
        if self.isEmpty() :
            return -1 
        else:
            popped = self.head.value
            self.head = self.head.next
            return popped
    
    def top(self):
        if self.isEmpty():
                return -1
        return self.head.value

# Usage example:
stack = Stack()
printTime(start)
print(stack.isEmpty())
printTime(start)
stack.push(10)
print("stack.push(10)")
printTime(start)
print("stack.top() : "+str(stack.top()))
printTime(start)
stack.push(20)
print("stack.push(20)")
printTime(start)
print("stack.top() : "+str(stack.top()))
printTime(start)
stack.push(30)
print("stack.push(30)")
printTime(start)
print("stack.top() : "+str(stack.top()))
printTime(start)
stack.push(40)
print("stack.push(40)")
printTime(start)
print("stack.top() : "+str(stack.top()))
printTime(start)
print(stack.isEmpty())
printTime(start)
print("stack.pop() : "+str(stack.pop()))
printTime(start)
print("stack.pop() : "+str(stack.pop()))
printTime(start)
print("stack.pop() : "+str(stack.pop()))
printTime(start)
print("stack.pop() : "+str(stack.pop()))
printTime(start)
print(stack.isEmpty())
# End : Code
printTime(start)
