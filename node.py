class Node:
	def __init__(self, value):
		self.value = value 
		self.children = set()

	def add_child(self, child_node):
		self.children.add(child_node) 
		
	def remove_child(self, child_node):
		self.children.discard(child_node)
