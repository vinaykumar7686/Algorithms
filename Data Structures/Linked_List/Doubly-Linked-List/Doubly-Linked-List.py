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

    def print_rev(self):
        if self.head == None:
            print('List Empty')
            return
        else:
            print("List in reverse order: ")
            def rev(point):
                if point:
                    rev(point.next)
                    print(point.data)
                else:
                    return

            rev(self.head)

    def insert_after(self,new_data, prev_node):
        '''
        Method to insert a node with data new_data after the node prev_node
        new_data is value to be stored in node
        prev_node is the node after which this new node is to be inserted
        '''
        ptr = Node(new_data)
        if prev_node is None:
            print('Invalid Node!')
        else:
            ptr.next = prev_node.next
            prev_node.next = ptr
            ptr.prev = prev_node
            
            if ptr.next is not None:
                ptr.next.prev = ptr

    def insert_before(self,new_data, nxt_node):
        '''
        Method to insert a node with data new_data before the node nxt_node
        new_data is value to be stored in node
        nxt_node is the node before which this new node is to be inserted
        '''
        
        if nxt_node is None:
            print('Invalid Node!')
        else:
            ptr = Node(new_data)
            if nxt_node.prev  == None:
                nxt_node.prev = ptr
                self.head = ptr
                ptr.next = nxt_node
            else:
                ptr.next = nxt_node
                ptr.prev = nxt_node.prev
                nxt_node.prev.next = ptr
                nxt_node.prev = ptr

    def delete_node(self, np):
        '''
        delete np node from the list
        '''
        if np is None or self.head is None:
            print('Unable to delete!')
        else:
            if np.next == None:
                np.prev.next = None
            elif np == self.head:
                self.head = np.next
                np.next.prev = None
            else:
                np.prev.next = np.next
                np.next.prev = np.prev
            
            print('Node Deleted')
            # Garbage collection
            import gc
            gc.collect()

dll = DLL()
dll.print_list()
dll.push_beg(1)
dll.append(2)
dll.print_list()

dll.print_rev()

dll.insert_before(0, dll.head.next)

dll.print_list()

dll.delete_node(dll.head.next)
dll.print_list()
