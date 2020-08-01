class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None
    
    def bft(self):
        if self.head == None:
            return
        print("Bredth First Traversal")
        ptr = self.head
        stack = [self.head]
        while stack:
            ptr = stack[0]
            stack = stack[1:]
            print(ptr.data)

            if ptr.left:
                stack.append(ptr.left)
            if ptr.right:
                stack.append(ptr.right)
                

    def pre_order_Traverse(self):
        if self.head == None:
            return
        
        temp = self.head

        stack = [self.head]

        print('Pre-Order')
        while stack:
            temp = stack[0]
            print(temp.data)
            stack = stack[1:]
            if temp.right != None:
                stack.insert(0,(temp.right))
            if temp.left != None:
                stack.insert(0,(temp.left))

    def in_order_Traverse(self):
        if self.head == None:
            return
                
        def trav(node):
            if node == None:
                return
            trav(node.left)
            print(node.data)
            trav(node.right)
        print('In-order')
        trav(self.head)
    
    def post_order_Traverse(self):
        if self.head == None:
            return
                
        def trav(node):
            if node == None:
                return
            
            trav(node.left)
            trav(node.right)
            print(node.data)
        print('Post-order')
        trav(self.head)
    
    def insert(self, data):
        ptr = Node(data)
        if self.head == None:
            self.head = ptr
            return
        
        stack = [self.head]
        while stack:
            temp = stack[0]
            stack = stack[1:]
            
            if not temp.right:
                temp.right = ptr
                break
            else:
                stack.insert(0, temp.right)
            if not temp.left:
                temp.left = ptr
                break
            else:
                stack.insert(0, temp.left)
    
    def delete_val(self, val):
        '''
        method to delete a given value from binary tree.
        Metodology: Copy the value of right most nodes` value in right subtree to the vnode whose value is to be deleted and delete the rightmost node
        '''
        if self.head == None:
            return
        if self.head.left == None and self.head.right==None:
            if self.head.data==val:
                self.head = None
                return
            return
        def delete_deepest(node, delnode):
            stack = [node]
            while stack:
                temp = stack[0]
                stack = stack [1:]

                if temp.right:
                    if temp.right == delnode:
                        temp.right = None
                    else:
                        stack.insert(0, temp.right)
                if temp.left:
                    if temp.left == delnode:
                        temp.left = None
                    else:
                        stack.insert(0, temp.left)
        
        stack = [self.head]
        temp = None
        key_node = None
        while stack:
            temp = stack.pop(0)
            if temp.data == val:
                key_node = temp
            if temp.right!=None:
                stack.insert(0, temp.right)
            if temp.left!=None:
                stack.insert(0, temp.left)
        
        if key_node:
            x = temp.data
            delete_deepest(self.head, temp)
            key_node.data = x
            





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

    tree.pre_order_Traverse()
    tree.in_order_Traverse()
    tree.post_order_Traverse()
    tree.insert(9)
    tree.in_order_Traverse()
    tree.bft()
