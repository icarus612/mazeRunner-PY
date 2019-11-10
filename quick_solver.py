from maze import Maze
from runner import Runner
import sys

saveFile = "completed.txt"

def open_and_build(file):
	with open(file) as m:
		txt = m.read()
		m1 = [list(i) for i in txt.split("\n")]
		flat = [y for x in m1 for y in x]
		s = set(txt)
		wall = txt[0][0]
		s.remove("\n")
		s.remove(wall)
		for i in s:
			if flat.count(i) == 1:
				pass
			else: 
				space = i
		s.remove(space)
		flat[:] = [x for x in flat if x != wall and x != space]
		start = flat[0]
		end = flat[1]
		return Maze(m1, start, end, wall, space)

if len(sys.argv) == 1:
	maze = Maze()
elif len(sys.argv) == 2:
	maze = open_and_build(sys.argv[1])
elif len(sys.argv) == 3:
	try:
		maze = Maze(build=(int(sys.argv[1]), int(sys.argv[2])))	
	except:
		maze = open_and_build(sys.argv[1])
		saveFile = sys.argv[2]
else:
	maze = Maze(build=(int(sys.argv[1]), int(sys.argv[2])))	
	saveFile = sys.argv[3]

maze.view_layout()
runner = Runner(maze)
runner.make_node_paths()
complete = "Yes" if runner.completed else "No"
print(f"Is maze possible? {complete}")

if runner.completed:	
	runner.build_path()
	runner.view_completed()
	with open(saveFile, "w") as file:
		file.write("Origional maze: \n")
		for i in maze.layout:
			for j in i:
				file.write(j)
			file.write("\n")
		file.write("\n Solved maze: \n")
		for i in runner.mapped_maze:
			for j in i:
				file.write(j)
			file.write("\n")
		file.write("\n")