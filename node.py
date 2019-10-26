import copy

class Node:
	def __init__(self, value):
		self.value = value 
		self.children = []
		self.visited = []

	def add_visited(self, node):
		self.visited.append(copy.deepcopy(node))	
	
	def add_child(self, child_node):
		self.children.append(copy.deepcopy(child_node))
		
	def add_path(self, node_path):
		if not self.path:
			self.path = node_path
		else:
			self.path = self.path if len(self.path) < len(node_path) else node_path

	def remove_child(self, child_node):
		self.children.discard(child_node)
