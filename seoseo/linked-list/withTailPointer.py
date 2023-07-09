import math
import time

from dll import *

start = time.time()  # save start time
def printTime(start):
    print("runtime :", time.time() - start)  # current time - start time = runtime


# Test

myList = DoublyLinkedList()
print("First List : ", end=" ")
print(myList)

for i in range(100000):
    myList.insertBefore(i)

print("After insertBefore(100000) : ")
printTime(start)

myList2 = DoublyLinkedList()
for i in range(100000):
    myList2.insertAfter(i)

print("After insertAfter(100000) : ")
printTime(start)
