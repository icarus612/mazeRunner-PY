class Node:
	def __init__(self, value):
		self.value = value 
		self.children = set()
		self.path = set()

	def add_child(self, child_node):
		self.children.add(child_node) 
		
	def add_path(self, node_path):
		self.path = node_path

	def remove_child(self, child_node):
		self.children.discard(child_node)