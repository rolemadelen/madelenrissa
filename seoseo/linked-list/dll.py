import math
import time
import sys
import pdb

start = time.time()  # save start time
def printTime():
    print("runtime :", time.time() - start)  # current time - start time = runtime
    start = time.time() 


class DoubleNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev # prev for pointing the previous node
        self.next = next

    def __str__(self):
        return str(self.value)


class DoublyLinkedList : 
    def __init__(self, value = None):
        node = DoubleNode(value) # create an empty list with only dummy node
        self.head = node
        self.length = 1

    def __iter__(self): # declare iterator
        value = self.head.next
        while value != self.head:
            yield value
            value = value.next
    
    def __str__(self): 
        if self.head is None:
            return "Empty List!\n"
        node = self.head
        string = ""
        while node.next :
            string += str(node.value) + "=> "
            node = node.next
        return string + str(node.value)

    def size(self) -> int : 
        return self.length
    
    def isEmpty(self):
        return True if self.size != 0 else False

    def splice(self, first, second, newValue):
        if first == None or second == None or newValue == None:
            return None
        # split the first and second
        first.prev.next = second.next
        second.next.prev = first.prev
        newValue.next.prev = second
        # insert value 
        second.next = newValue.next
        first.prev = newValue
        newValue.next = second
        self.nodeCount += 1

    def moveBefore(self, first, newValue) : 
        self.splice(first, first, newValue.prev)

    def moveAfter(self, first, newValue) : 
        self.splice(first, first, newValue)

    def insertBefore(self, first, newValue):
        self.moveBefore(DoubleNode(newValue), first)
    
    def insertAfter(self, first, newValue):
        self.moveAfter(DoubleNode(newValue), first)
