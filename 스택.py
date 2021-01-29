#LIFO, 스택, 연결리스트
class Node:
    def __init__(self,item, next = None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None

    def push(self,item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item
a = Stack()
