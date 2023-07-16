import time

start = time.time()  # save start time
def printTime(start):
    print("runtime :", time.time() - start)  # current time - start time = runtime


class Stack:
    def __init__(self):
        self.stack = []  # empty list for stack

    def push(self, item):
        self.stack.append(item)  # push as append

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()  # 
        else:
            return None

    def top(self):
        if not self.isEmpty():
            return self.stack[-1]  # return top
        else:
            return None

    def isEmpty(self):
        return len(self.stack) == 0


print("Stack with Array")
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

