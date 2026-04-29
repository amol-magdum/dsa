class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


drinks = Node("drinks")
hot = Node("hot")
cold = Node("cold")
tea = Node("tea")
coffee = Node("coffee")
fanta = Node("fanta")
cola = Node("fanta")

hot.left = tea
hot.right = coffee

cold.left = cola
cold.right = fanta

drinks.left = hot
drinks.right = cold

print(drinks.val)
print(drinks.left.val)
print(drinks.right.left.val)