# Word 'head' it means Node and 'data' means data field in that Node and 'next' means next field in that Node
'''
-----------------
| data  | next  |   = Node
-----------------
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_llist(self):
        '''
        Function to print Linked List
        '''
        temp=self.head
        if temp==None:
            print("Linked List Empty")
        else:
            while temp:
                print(temp.data)
                temp=temp.next

    def push(self, item):
        '''
        Function to add a node at the beginning of linkedlist
        '''
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def append(self, item):
        '''
        Function to add a node at the end of linkedlist
        '''

        new_node= Node(item)
        if self.head == None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node

    def insertAfter(self, prev_node, item):
        '''
        Function to insert the node after the prev_node sent as parameter
        '''

        # checking if prev_node is actually a node

        if prev_node == None:
            print('Given node is not a linkedlist')

        else:
            new_node = Node(item)
            new_node.next = prev_node.next
            prev_node.next=new_node

    def delete_key(self, key):
        '''
        To delete all the occurance of value sent as key to the function.
        '''
        temp=self.head
        
        if temp==None and key==None:
            return
        elif temp is not None and key is temp.data:
            self.head=temp.next
        else:
            prev=temp
            while temp:
                if temp.data==key:
                    break
                prev= temp
                temp=temp.next
             
            if temp is None:
                print('Key not found')
                return

            prev.next= temp.next

    def delete_pos(self, pos):
        '''
        To delete the node at given position in linked list
        '''
        # If linked list is empty 
        if self.head == None: 
            return 
  
        # Store head node 
        temp = self.head 
  
        # If head needs to be removed 
        if pos == 0: 
            self.head = temp.next
            temp = None
            return 
  
        # Find previous node of the node to be deleted 
        for i in range(pos-1 ): 
            temp = temp.next
            if temp is None: 
                break
  
        # If position is more than number of nodes 
        if temp is None: 
            return 
        if temp.next is None: 
            return 
  
        # Node temp.next is the node to be deleted 
        # store pointer to the next of node to be deleted 
        next = temp.next.next
  
        # Unlink the node from linked list 
        temp.next = None
  
        temp.next = next 

    def list_size_i(self):
        '''
        Iterative approach of finding size of a  linked list.
        '''
        if self.head == None:
            return 0
        else:
            temp = self.head
            size = 0
            while temp:
                temp = temp.next
                size+=1
            return size

    def size_rec(self, temp):
        '''
        Size of linkedlist through iterative approach
        '''
        if temp:
            return 1+self.size_rec(temp.next)
        else:
            return 0

    def list_size_r(self):
        '''
        Driver for size_rec that finds size of linkedlist through iterative approach
        '''
        return(self.size_rec(temp = self.head))

    def exists(self, val):
        '''
        Returns True if val exists in linked list else False
        '''
        if self.head==None:
            return False
        else:
            temp = self.head
            while temp:
                if str(temp.data) == str(val):
                    return True
                temp = temp.next
            return False


    
if __name__ == "__main__":
    
    ll=LinkedList()

    ll.push('b')
    ll.push('a')

    ll.append('c')

    ll.insertAfter(ll.head.next, 'ab')

    #ll.delete_key('ab')
    ll.delete_pos(1)
    # In above line ll.head signifies First Node, ll.head.next points to Second Node and so on
    ll.print_llist()

    print(f'Size of list : {ll.list_size_r()}')

    print(f'"x" exists in linked list : {ll.exists(val = "x")}')
    print(f'"a" exists in linked list : {ll.exists(val = "a")}')




    

