from maze_runner import Maze, Runner
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-of", "--openfile", help="Open File Name", dest='openfile', type=str)
parser.add_argument("-sf", "--savefile", help="Save File Name", dest='savefile', type=str, default='completed.txt')
parser.add_argument("-xy", "--dimensions", help="Maze dimentions", dest='dimensions', type=int, nargs=2)
parser.add_argument("-mt", "--type", help="Maze Type", dest='type', type=str, default='h')

args = parser.parse_args()
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

if args.openfile:
	maze = open_and_build(sys.argv[1])
elif args.dimensions:
	maze = Maze(build=(int(args.dimensions[0]), int(args.dimensions[1])), build_type=args.type)	
else:
	maze = Maze(build_type=args.type)	

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
		