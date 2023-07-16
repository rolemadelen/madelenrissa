import math
import time

from dll import *
from sll import *

start = time.time()  # save start time
def printTime(start):
    print("runtime :", time.time() - start)  # current time - start time = runtime


# Test

myList = DoublyLinkedList()
print("First List : ", end=" ")
print(myList)

for i in range(1, 100001):
    myList.insertBefore(i, i*2)

print("After insertBefore(100000) : ")
printTime(start)

myList2 = DoublyLinkedList()
for i in range(1, 100001):
    myList2.insertAfter(i, i*3)

print("After insertAfter(100000) : ")
printTime(start)
