
class Node:
	def __init__(self, value=None):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self, node=None):
		self.head = node
		self.tail = node

	def insert(self, new_node):
		if self.head is None:
			self.head = new_node
			self.tail = new_node

	def display(self):
		node = self.head
		while node:
			yield node.value
			node = node.next

node1 = Node('fabio')
ll = LinkedList(node1)