class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None
    
    def in_order_Traverse(self):
        if self.head == None:
            return
        
        temp = self.head

        stack = [self.head]

        while stack:
            temp = stack[-1]
            print(temp.data)

            if temp.left != None:
                stack.insert(0 , (temp.left))
            if temp.right != None:
                stack.insert( 0 ,(temp.right))

            stack.pop()

if __name__ == "__main__":
    tree = Tree()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)

    tree.head = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n4.left = n6
    n5.right = n7
    n7.left = n8

    tree.in_order_Traverse()
