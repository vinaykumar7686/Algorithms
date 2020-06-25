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
    
if __name__ == "__main__":
    
    ll=LinkedList()

    ll.push('b')
    ll.push('a')

    ll.append('c')

    ll.insertAfter(ll.head.next, 'ab')
    # In above line ll.head signifies First Node, ll.head.next points to Second Node and so on
    ll.print_llist()



    

