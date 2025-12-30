# singly list operations
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def traverse(self):
        if not self.head:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next

    def insert_at(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        prev_pos = None
        count = 0 
        while count < position and current is not None:
            prev_pos = current
            current = current.next
            count += 1
        prev_pos.next = new_node
        new_node.next = current

    def delete_value(self, val):
        current = self.head
        prev = None
        while current is not None:
            if current.data == val:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return
# test cases for singly linked list operations
sll = SinglyLinkedList()    
sll.append(1)
sll.append(2)
sll.append(4)
sll.traverse()