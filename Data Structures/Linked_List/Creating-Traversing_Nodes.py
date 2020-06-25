class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_llist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next


if __name__ == '__main__':
    
    #Creating instance of LinkedList class
    ll=LinkedList()

    # Creating Node
    ll.head=Node('a')
    first=Node('b')
    second=Node('c')
    third=Node('d')

    # Connecting Nodes
    ll.head.next=first
    first.next=second
    second.next=third

    # Printing elements of linked list
    ll.print_llist()
    




    
