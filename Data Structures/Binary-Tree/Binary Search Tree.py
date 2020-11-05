class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self):
        self.head = None
        
    def create(self, nums):
        for num in nums:
            
            ptr = Node(num)
            
            if not self.head:
                self.head = ptr
            else:
                temp = self.head
                while temp:
                    if temp.data>num:
                        if not temp.left:
                            temp.left = ptr
                            break
                        else:
                            temp = temp.left
                    else:
                        if not temp.right:
                            temp.right = ptr
                            break
                        else:
                            temp = temp.right
    
    def print_tree(self):
        
        if not self.head:
            return []
        
        else:
            ans = []
            def trav(root):
                if not root:
                    return
                
                trav(root.left)
                ans.append(root.data)
                trav(root.right)
                
            trav(self.head)
            return ans
                
            
            
            
        
        
    

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        
        n = int(input())
        nums = list(map(lambda x: int(x), (input()).split()))
        t = Tree()
        t.create(nums)
        print(t.print_tree())
                            
                    
