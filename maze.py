import random

class Maze:
	def __init__ (self, maze=[[]]):
		self.width = len(maze[0])
		self.height = len(maze)
		self.maze = maze
		self.start = None
		self.end = None
		
	def make_maze(self, height, width, maze_type = "h"):
		self.height = height
		self.width = width
		self.maze = [[(h, w) for w in range(width)] for h in range(height)]
		open_points = []
		for x in range(len(self.maze)):
			for y in range(len(self.maze[x])):
				p = self.maze[x][y]
				if p[0] == 0 or p[1] == 0 or p[0] == height-1 or p[1] == width-1:
					self.maze[x][y] = "#"
				else:
					open_points.append((x,y))
		if maze_type == "h":
			s= (1, random.choice(range(1, width-1)))
			e = (height-2, random.choice(range(1, width-1)))
			del open_points[open_points.index(s)]
			del open_points[open_points.index(e)]
		elif maze_type == "v":
			s = (random.choice(range(1, height-1)), 1)
			e = (random.choice(range(1, height-1)), width-2)
			del open_points[open_points.index(s)]
			del open_points[open_points.index(e)]
		elif maze_type == "r":
			s = random.choice(open_points)
			del open_points[open_points.index(s)]
			e = random.choice(open_points)
			del open_points[open_points.index(e)]
		else:
			raise ValueError("Incorrect Maze type. (try h, v, or r)")
		self.maze[s[0]][s[1]] = "s"
		self.maze[e[0]][e[1]] = "e"
		for i in open_points:
			self.maze[i[0]][i[1]] = random.choice([" ", " ", "#"])

	def see_maze(self):
		for i in self.maze:
			print(i)
	
	def find_end_points(self):
		for x in range(len(self.maze)):
			for y in range(len(self.maze[x])):
				p = self.maze[x][y]
				if p == "s" or p == "S":
					self.start = (x, y)
				elif p == "e" or p == "E":
					self.end = (x, y)

	def runner(self):
		self.find_end_points()
		current_route = []
		checked_paths = []
		possible_routes = []
		print(self.maze[self.start[0]][self.start[1]])

	def maze_stats(self):
		self.find_end_points()
		print(f"	start: {self.start} \n	end: {self.end}\n	size: {self.height} x {self.width}")
