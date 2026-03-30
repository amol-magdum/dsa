class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def push (self, item):
        self.items.append(item)

    def pop(self):
        if len (self.items) == 0:
            return "pop failed, stack is empty"
        x = self.items.pop()
        return x

    def top(self):
        if len (self.items) == 0:
            return "top failed, stack is empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)

stack = Stack()
print(stack.isEmpty())
stack.push(5)
stack.push(10)
stack.push(20)
print(stack.isEmpty())

print(f"Stack contents = {stack.items}")
print(f"poped item = {stack.pop()}")
print(f"Stack after pop = {stack.items}")
