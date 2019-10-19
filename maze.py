import random
class Maze:
	def __init__ (self, maze=[]):
		self.width = None
		self.height = None
		self.start = None
		self.end = None
		self.maze = maze
		
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
			self.start = (1, random.choice(range(1, width-1)))
			self.end = (height-2, random.choice(range(1, width-1)))
			del open_points[open_points.index(self.start)]
			del open_points[open_points.index(self.end)]
		elif maze_type == "v":
			self.start = (random.choice(range(1, height-1)), 1)
			self.end = (random.choice(range(1, height-1)), width-2)
			del open_points[open_points.index(self.start)]
			del open_points[open_points.index(self.end)]
		elif maze_type == "fse":
			self.start = random.choice(open_points)
			del open_points[open_points.index(self.start)]
			self.end = random.choice(open_points)
			del open_points[open_points.index(self.end)]
		else:
			raise ValueError("Incorrect Maze type. (try h, v, or fse)")
		self.maze[self.start[0]][self.start[1]] = "s"
		self.maze[self.end[0]][self.end[1]] = "e"
		for i in open_points:
			self.maze[i[0]][i[1]] = random.choice([" ", " ", "#"])
					
	def find_end_points(self, maze):
		for x in range(len(maze)):
			for y in range(len(maze[x])):
				p = maze[x][y]
				if p == "s" or p == "S":
					self.start = (x, y)
				elif p == "e" or p == "E":
					self.end = (x, y)

	def see_maze(self):
		for i in self.maze:
			print(i)

	def maze_stats(self):
		print(f"	start: {self.start} \n	end: {self.end}\n	size: {self.height} x {self.length}")
