from maze import Maze
from runner import Runner

m1 = [	['#','#','#','#','#','#','#','#','#'], 
		['#','s','#',' ',' ',' ','#','e','#'], 
     	['#',' ','#',' ','#',' ',' ',' ','#'], 
     	['#',' ',' ',' ','#',' ','#',' ','#'], 
     	['#','#','#','#','#','#','#','#','#']] 

maze = Maze(layout=m1)

#maze.build_new(15, 20)
runner = Runner(maze)
maze.view_layout()
runner.make_node_paths(runner.start)
