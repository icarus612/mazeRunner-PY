from maze import Maze
from runner import Runner
import sys
import numpy as np

try:
	with open(sys.argv[1]) as m:
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
		maze = Maze(m1, start, end, wall, space)
		
except IndexError:
	maze = Maze()

maze.view_layout()
runner = Runner(maze)
runner.make_node_paths()
if runner.can_run():
	runner.build_path()
else:
	print(runner.completed)
