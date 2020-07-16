class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
    
class DLL:
    def __init__(self):
        self.head = None

    def push_beg(self, val):
        ptr = Node(val)

        if self.head == None:
            self.head = ptr
        else:
            ptr.next = self.head
            self.head.prev = ptr
            self.head = ptr

        print(f'{val} added to the beginning of the list')

    def append(self, val):
        ptr = Node(val)
        if self.head == None:
            self.head = ptr
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = ptr
            ptr.prev = temp
        print(f'{val} appended to the list')

    def print_list(self):
        if self.head == None:
            print("List Empty")
        else:
            print('Current status of List is as follows')
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next

dll = DLL()
dll.print_list()
dll.push_beg(1)
dll.append(2)
dll.print_list()
