import Node
class Runner:
	def __init__(self, maze):
		self.nodes = []
		self.node_paths = []
		self.current_route = []
		self.checked_paths = []
		self.possible_routes = []
		self.start = None
		self.end = None
		self.maze = maze

	def get_nodes(self):
		p = self.maze.layout
		for x in range(len(p)):
			for y in range(len(p[x])):
				if p[x][y] == " ":
					self.nodes.add((x,y))

	def find_end_points(self):
		for x in range(len(self.maze.layout)):
			for y in range(len(self.maze.layout[x])):
				p = self.maze.layout[x][y]
				if p == self.maze.start_char:
					self.start = (x, y)
				elif p == self.maze.end_char:
					self.end = (x, y)
	def add_node(self):
		
	def make_node_paths(self):
		self.find_end_points()
		self.get_nodes()
		for i in self.nodes:
			print(i)
		


class LinkedList:
	def __init__(self, value=None):
		self.head_node = Node(value)

	def get_head_node(self):
		return self.head_node

	def insert_beginning(self, new_value):
		new_node = Node(new_value)
		new_node.add_child(self.head_node)
		self.head_node = new_node

	def remove_node(self, value_to_remove):
		current_node = self.get_head_node()
		if current_node.value() == value_to_remove:
			self.head_node = current_node.traverse()
		else:
			while current_node:
				next_node = current_node.traverse()
				if next_node.value() == value_to_remove:
					current_node.add_child(next_node.traverse())
					current_node = None
				else:
					current_node = next_node