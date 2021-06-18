class Node:
	def __init__(self, value):
		self.value = value
		self.next = None  

# I could do it manually like:
node1 = Node('a')
# node1.value = 'a'
# node1.next = None

node2 = Node('b')
# node2.value = 'b'
# node2.next = None

# and now link then
node1.next = node2
# node1.value = 'a'
# node1.next = node2

node3 = Node('c')

node2.next = node3
# head       = node1
# node1.next = node2
# node2.next = node3
# node3.next = None   (last node of the linked list)
