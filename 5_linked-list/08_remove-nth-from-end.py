# remove nth element from end of singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def remove_nth_from_end(self, n):
        slow = self.head
        fast = self.head
        for _ in range(n):
            fast = fast.next
        
        if fast is None:
            return fast.next
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return self.head
    
#time complexity: O(L) where L is the length of linked list
#space complexity: O(1)
        
