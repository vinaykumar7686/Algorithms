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

    def search(self, val):
        '''
        Returns the index of element in linked list
        '''  
        if self.head == None:
            return
        else:
            temp = self.head
            count = 1
            while temp:
                if temp.data == val:
                    return count
                temp = temp.next
                count+=1
        return

    def nth_node_i(self, n):
        '''
        Function to find nth number in list iteratively.
        '''
        if self.head == None or n<0:
            return
        else:
            count = 1
            temp = self.head
            while temp:
                if count == n:
                    return temp.data
                temp = temp.next
                count+=1
            return

    def rec_nth_node(self, temp, x, n):
        
        if temp == None or x>n:
            return
        elif x==n:
            return temp.data
        else:
            return self.rec_nth_node(temp.next, x+1, n)

    def nth_node_r(self, n):
        '''
        Function to find nth number in list recursively
        '''
        if self.head==None:
            return
        return self.rec_nth_node(self.head, 1, n)

    def nth_node_end(self, n):
        '''
        Function to find nth number in list from end iteratively.
        '''
        if self.head == None or n<0:
            return
        else:
            # Storing size of list in variable size
            size = ll.list_size_i()
            # Calculating position from the front
            n = size - n + 1
            # Using pre-created function that finds nth number from front
            return ll.nth_node_i(n)

    def nth_node_end_x(self, n):
        '''
        Advanced approach to finding nth value from end using 2 pointers
        '''
        if self.head == None or n<1:
            return
        else:
            main = self.head
            ref = self.head
            count = 0
            while count<n:
                if ref==None:
                    return
                
                ref = ref.next
                count+=1
            
            while ref:
                ref = ref.next
                main = main.next

            return main.data

    def mid_ele(self):
        '''
        Returns middle element of the list
        if list has even number of elements then it returns a tuple containing mid elements.
        '''
        size = self.list_size_i()
        if size%2==0:
            return (self.nth_node_i(int(size/2)), self.nth_node_end(int(size/2)))
        else:
            return self.nth_node_i(int(size/2)+1)

    def count_occ(self, val: str)-> int:
        '''
        Counts the occurance of a value in the list
        '''
        if self.head == None:
            return 0
        else:
            count = 0
            temp = self.head
            while temp:
                if temp.data == val:
                    count +=1
                temp = temp.next
            return count
			
    def test_cycle(self)->bool:
        '''
        This method tests for presense of cycle in the linked list
        '''
        if self.head == None:
            return False
        else:
            temp = self.head
            nodes = set()
            while temp:
            
                if temp in nodes:
                    return True
                nodes.add(temp)
                temp = temp.next
        
            return False
    
    def test_cycle_x(self)->bool:
        '''
        Floyd’s Cycle-Finding Algorithm
        Approach: This is the fastest method and has been described below:

        Traverse linked list using two pointers.
        Move one pointer(slow) by one and another pointer(fast) by two. 
        If these pointers meet at the same node then there is a loop. 
        If pointers do not meet then linked list doesn’t have a loop.
        '''
        if self.head==None:
            return False
        else:
            slow = self.head
            fast = self.head

            while slow and fast and fast.next:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    return True
            return False
    
    def check_palin(self):
        '''
        Method to check wheter a linked list in palindrome or not
        '''
        if self.head == None:
            return False
        else:
            stack = list()
            temp = self.head
            while temp:
                stack.append(temp.data)
                temp = temp.next
            
            temp = self.head
            while temp:
                if not temp.data == stack.pop():
                    return False
                temp = temp.next
            return True
    
    def remove_duplicates(self):
        '''
        Method to remove duplicacy in a list
        '''
        if self.head == None:
            return
        else:
            temp = self.head
            while temp:
                # storing value of current node in a variable for comparison
                val = temp.data
                # initilising a pointer to traverse through remaining list in search of duplicates
                trav = temp
                while trav.next:
                    #initialising a poiter to point to previous node, so as to enable us to remove a duplicate node
                    prev = trav
                    trav = trav.next
                    if trav.data == val:
                        prev.next = trav.next
                temp = temp.next
        
    def remove_duplicates_x(self):
        '''
        Advanced approach to removing duplicates in a linked list using a set
        '''
        if self.head == None:
            return
        else:
            temp = self.head
            # initialising a set named tab to save the elements occured in the list so far
            tab = set()
            tab.add(temp.data)

            while temp.next:
                prev = temp
                temp = temp.next
                # if the data of node is present in the set the removing the node
                if temp.data in tab:
                    prev.next = temp.next
                # else adding the value to the set
                else:
                    tab.add(temp.data)


if __name__ == "__main__":
    
    ll=LinkedList()

    ll.push('b')
    ll.push('a')

    ll.append('c')
    ll.append('z')
    ll.append('z')

    ll.insertAfter(ll.head.next, 'ab')

    #ll.delete_key('ab')
    ll.delete_pos(1)
    # In above line ll.head signifies First Node, ll.head.next points to Second Node and so on
    ll.print_llist()

    print(f'Size of list : {ll.list_size_r()}')

    print(f'"x" exists in linked list : {ll.exists(val = "x")}')
    print(f'"a" exists in linked list : {ll.exists(val = "a")}')

    print(f'Search for {"ab"} finished at: {ll.search("ab")}')

    print(f'2nd element in list is : {ll.nth_node_r(2)}')

    print(f'2nd element from ending in list is : {ll.nth_node_end_x(2)}')

    print(f'Mid Element of array is/are : {ll.mid_ele()}')

    print(f'"z" occours in list : {ll.count_occ("z")} times')

    print (f'Cycles in list : {ll.test_cycle_x()}')

    print(f'Is linked list a palindrome: {ll.check_palin()}')

    print("Before removing duplicacy ")
    ll.print_llist()

    ll.remove_duplicates_x()
    print("After removing duplicacy ")
    ll.print_llist()

    

