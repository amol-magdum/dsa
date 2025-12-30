# Find Pairs with given Sum in Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __init__(self):
        self.head = None

    def find_pairs_with_sum(self, target_sum):
        result = []
        left = self.head
        right = self.head
        while right.next:
            right = right.next

        while left and right and left < right:
            total = left.data + right.data
            if total == target_sum:
                result.append((left.data, right.data))
                left = left.next
                right = right.prev

            if total > target_sum:
                right = right.prev
            else:
                left = left.next

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
