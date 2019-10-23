from node import Node
class Runner:
	def __init__(self, maze):
		self.open_nodes = []
		self.node_paths = []
		self.start = None
		self.end = None
		self.maze = maze

	def get_open_nodes(self):
		p = self.maze.layout
		for x in range(len(p)):
			for y in range(len(p[x])):
				if p[x][y] == self.maze.open_char:
					self.open_nodes.append(Node((x, y)))

	def find_end_points(self):
		for x in range(len(self.maze.layout)):
			for y in range(len(self.maze.layout[x])):
				p = self.maze.layout[x][y]
				if p == self.maze.start_char:
					self.start = Node((x, y))
				elif p == self.maze.end_char:
					self.end = Node((x, y))

	def look_around(self, node):
		for i in self.open_nodes:
			if i.value[0]-1 == node.value[0] and i.value[1] == node.value[1]:
				node.add_child(i)
			elif i.value[0]+1 == node.value[0] and i.value[1] == node.value[1]:
				node.add_child(i)
			elif i.value[1]-1 == node.value[1] and i.value[0] == node.value[0]:
				node.add_child(i)
			elif i.value[1]+1 == node.value[1] and i.value[0] == node.value[0]:
				node.add_child(i)
		for i in node.children:
			print(i.value)

	def make_node_paths(self):
		self.find_end_points()
		self.get_open_nodes()
		print(self.start.value)
		self.look_around(self.start)