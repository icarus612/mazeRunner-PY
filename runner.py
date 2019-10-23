from node import Node
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
					self.nodes.append(Node())

	def find_end_points(self):
		for x in range(len(self.maze.layout)):
			for y in range(len(self.maze.layout[x])):
				p = self.maze.layout[x][y]
				if p == self.maze.start_char:
					self.start = (x, y)
				elif p == self.maze.end_char:
					self.end = (x, y)
	def add_node(self, value):
		self.nodes.append
	def make_node_paths(self):
		self.find_end_points()
		self.get_nodes()
		for i in self.nodes:
			print(i)
		
