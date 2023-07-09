import math
import time
import sys
import pdb

start = time.time()  # save start time
def printTime():
    print("runtime :", time.time() - start)  # current time - start time = runtime
    start = time.time() 

# Class for Node - single
class Node:
    def __init__(self, value) -> None:
        self.value = value # pointing the value == attribute
        self.next = None # next for pointing the following node

# To access a linked list, it must have a head that indicates the first node. 

# head = Node(0)
# head.next = Node(1)
# head.next.next = Node(2)

# node = head
# while node : 
#     print(node.data, end = " | ")
#     node = node.next

# Class for Linked List
class LinkedList : 
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is None:
            return "Empty List!\n"
        node = self.head
        string = ""
        while node.next :
            string += str(node.value) + " -> "
            node = node.next
        return string + str(node.value)

    
    def __contains__(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False
    
    
    # instead of __len__ 
    def size(self) -> int : 
        return self.length


    def isEmpty(self) -> str :
        return True if self.head is None or self.size() == 0 else False


    def pushFront(self, value) : 
        node = Node(value)
        if self.head is None : 
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1


    def pushBack(self, value) : 
        node = Node(value)
        if self.head is None : 
            self.head = node
        else:
            prev = self.head
            while prev.next : 
                prev = prev.next
            prev.next = node
        self.length += 1


    def popFront(self):
        if self.head is None : 
            return None
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node.value


    def popBack(self):
        if self.head is None : 
            return None
        node = self.head
        if self.head.next is None:
            self.head = None
        else:
            while node.next is not None:
                prev = node
                node = node.next
            prev.next = None
        self.length -= 1
        return node.value
    

    def getFront(self) : 
        if self.head is None : 
            return None
        node = self.head
        return node.value


    def getBack(self) : 
        if self.head is None : 
            return None
        node = self.head
        if self.head.next is None:
            self.head = None
        else:
            while node.next is not None:
                prev = node
                node = node.next
            prev.next = None
            return prev.next.value


    def reverse(self) : 
        if self.length <= 1 : 
            return None
        ahead = self.head.next
        prev = self.head
        prev.next = None
        while ahead :
            self.head = ahead
            ahead = ahead.next
            self.head.next = prev
            prev = self.head


    def insert(self, index, value) :
        if index <= 0 : 
            self.pushFront(self, value)
        elif index >= self.length:
            self.pushBack(self, value)
        else:
            prev = self.head
            for _ in range(index -1):
                prev = prev.next
            node = Node(value)
            node.next = prev.next
            prev.next = node
            self.length += 1
    
    
    def remove(self, value):
        if self.head.value == value : 
            self.popFront()
            return True

        prev = self.head
        while prev.next : 
            if prev.next.value == value:
                prev.next = prev.next.next
                self.length -= 1
                return True

            prev = prev.next
        return False

