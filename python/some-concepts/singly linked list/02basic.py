class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):  
		self.head = None # HEAD -> node1 -> node2 -> node3 -> None

	def insert_node(self, new_node):
		if self.head is None:
			self.head = new_node
		else:
			node = self.head
			while True: 
				if node.next is None: # last node which points to None
					break
				node = node.next 
			node.next = new_node # linking the new node in the last node.next value

ll = LinkedList()
# ll.head = None 

node1 = Node('a')
ll.insert_node(node1) 
# ll.head = node1
# ll.head.next = None

node2 = Node('b')
ll.insert_node(node2) 
# ll.head           = node1
# ll.head.next      = node2
# ll.head.next.next = None

node3 = Node('c')
ll.insert_node(node3) 
# ll.head           	 = node1
# ll.head.next      	 = node2
# ll.head.next.next 	 = node3
# ll.head.next.next.next = None

