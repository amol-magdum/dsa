# reverse the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:

    def __init__(self):
        self.head = None
    
    def reverse(self):
        temp = self.head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        self.head = prev
    
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

# test case for reversing linked list
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.traverse()
print("\nAfter reversing the linked list:")
sll.reverse()
sll.traverse()

