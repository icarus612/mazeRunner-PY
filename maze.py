maze = [['#','#','#','#','#','#','#','#','#'], 
     	['#','S','#',' ',' ',' ','#','E','#'], 
     	['#',' ','#',' ','#',' ',' ',' ','#'], 
     	['#',' ',' ',' ','#',' ','#',' ','#'], 
     	['#', '#','#','#','#','#','#','#','#']] 

class Maze:
	def __init__(self, maze):
		self.length = len(maze[0])
		self.height = len(maze)
		self.start
		self.end
		self.current_path = []
		self.visited = []
		self.wall = []
		self.open = []
		self.paths = []
	for x in range(maze):
		for y in range(maze[x]):
			p = maze[x][y]
			if p == " ":
				self.open = (x, y)
			elif p == "#":
				self.wall = (x, y)
			elif p == "s"
				self.start = (x, y)
			elif p == "e":
				self.end = (x, y)


