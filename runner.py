class Runner:
	def __init__(self, maze):
		self.current_route = []
		self.checked_paths = []
		self.possible_routes = []
		p = maze.find_end_points()
		self.start = p[0]
		self.end = p[1]
		self.maze = maze

	def find_end_points(self):
		for x in range(len(self.maze)):
			for y in range(len(self.maze[x])):
				p = self.maze[x][y]
				if p == self.start_char:
					start = (x, y)
				elif p == self.end_char:
					send = (x, y)

	