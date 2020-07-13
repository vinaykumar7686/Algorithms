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



# Driver program to test above function 

# Initialize list as empty 
cllist = CircularLinkedList() 

# Created linked list will be 11->2->56->12 
cllist.push(1)
cllist.push(12) 
cllist.push(56) 
cllist.push(2) 
cllist.push(11) 

print ("\nContents of circular Linked List")
cllist.printList() 

head1 = CircularLinkedList()
head2 = CircularLinkedList()
cllist.div(head1,head2)

print('\nContents of List 1')
head1.printList()
print('\nContents of List 2')
head2.printList()
