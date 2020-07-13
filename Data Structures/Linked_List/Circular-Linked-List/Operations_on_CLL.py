class Node: 
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class CircularLinkedList: 
	
	# Constructor to create a empty circular linked list 
	def __init__(self): 
		self.head = None

	# Function to insert a node at the beginning of a 
	def push(self, data): 
		ptr = Node(data) 
		temp = self.head 
		
        # making new node's next point to starting
		ptr.next = self.head 

		# If linked list is not None then set the next of last node 
		if self.head is not None: 
			while(temp.next != self.head): 
				temp = temp.next
			temp.next = ptr

		else: 
			ptr.next = ptr # For the first node 

		self.head = ptr 

	# Checking if a linked list is circular or not
	def is_circular(self):
		if self.head==None:
			return True
		else:
			temp = self.head
			while temp.next!=None:
				if temp.next == self.head:
					return True
				temp = temp.next
			return False

	# Function to convert a simple linked list ot circular linked list
	def set_circular(self):
		if self.head==None:
			return
		else:
			temp = self.head
			while temp.next != None:
				if temp.next == self.head:
					print('Already a circular linked list')
					return
				temp = temp.next
			temp.next = self.head

	# Function to convert a circular linked list to circular
	def set_linear(self):
		if self.head == None:
			return
		else:
			temp = self.head
			while temp.next != self.head:
				if temp.next == None:
					print('Already a linear linked list')
					return
				temp = temp.next
			temp.next = None

	# Function to count the number of nodes in circular linked list
	def count_nodes(self):
		if self.head == None:
			return 0
		else:
			count = 1
			temp = self.head
			while temp.next != self.head:
				count+=1
				temp = temp.next
			return count


	# Function to print nodes in a given circular linked list 
	def printList(self): 
		temp = self.head 
		if self.head is not None: 
			while(True): 
				print(temp.data) 
				temp = temp.next
				if (temp == self.head): 
					break

	# Function to divide Linked list into two
	def div(self, head1, head2):
		if self.head == None:
			return
		else:
			p1 = self.head
			p2 = self.head
			while p2.next != self.head and p2.next.next != self.head:
				p2 = p2.next.next
				p1 = p1.next
			
			if p2.next.next == self.head:
				p2 = p2.next
			
			head1.head = self.head

			if self.head.next!=None:
				head2.head = p1.next
			p2.next = p1.next

			p1.next = self.head
	
	def insert_sorted(self, val):
		ptr = Node(val)
		# for empty list
		if self.head == None:
			self.head = ptr
			ptr.next = self.head
		else:
			curr = self.head
			# for case when the new no. is smallest
			if curr.data>val:
				while curr.next != self.head:
					curr = curr.next
				ptr.next = self.head
				curr.next = ptr
				self.head = ptr
			# all cases excluding above
			else:
				while curr.next != self.head and curr.next.data<val:
					curr = curr.next
				ptr.next = curr.next
				curr.next = ptr





# Driver program to test above function 

# Initialize list as empty 
cllist = CircularLinkedList() 

# Created linked list will be 11->2->56->12 
cllist.push(7)
cllist.push(6) 
cllist.push(5) 
cllist.push(2) 
cllist.push(1) 

print ("\nContents of circular Linked List")
cllist.printList() 

'''head1 = CircularLinkedList()
head2 = CircularLinkedList()
cllist.div(head1,head2)

print('\nContents of List 1')
head1.printList()
print('\nContents of List 2')
head2.printList()'''

cllist.insert_sorted(0)
print('\nList after insertion')
cllist.printList()

print(f"This list is circular : {cllist.is_circular()}")

print(f'Total number of nodes in list : {cllist.count_nodes()}')

cllist.set_linear()
cllist.set_circular()
