import math
import time

from sll import *

start = time.time()  # save start time
def printTime(start):
    print("runtime :", time.time() - start)  # current time - start time = runtime


# Test

myList = LinkedList()
print("First List : ", end=" ")
print(myList)

for i in range(100000):
    myList.pushFront(i)

print("After pushFront(100000) : ")
printTime(start)

myList2 = LinkedList()
for i in range(100000):
    myList2.pushBack(i)

print("After pushBack(100000) : ")
printTime(start)

myList.reverse()
print("After Reverse : ")
printTime(start)