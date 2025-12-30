# reverse the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def odd_even_separation(self):

        if not self.head or not self.head.next:
            return
        odd  = self.head
        even = self.head.next
        even_head = even
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return self.head

    def find_length_of_loop(self):
            slow = self.head
            fast  = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    count = 1
                    current = slow
                    while current.next != slow:
                        count += 1
                        current = current.next
                    return count
            return 0

    def find_starting_point_of_loop(self):
        slow = self.head
        fast  = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
    
    def find_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

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

    def reverse(self):
        temp = self.head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        self.head = prev

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

