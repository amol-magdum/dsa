
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        
    def Insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def Insert_at(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.Insert_at_head(data)
            return
        temp = self.head
        count = 0 
        while temp and count < position - 1:
            temp = temp.next
            count += 1
        if not temp:
            print("Position out of bounds")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next: # If not inserting at the end
            temp.next.prev = new_node
        temp.next = new_node

    def reverse(self):
        if not self.head:
            return
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev
        