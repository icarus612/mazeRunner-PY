from maze_runner import Maze, Runner
import re

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

def find_type():
	maze_type = input("Would you like to upload a maze or build a new one? \n  1) Build New \n  2) Upload \n").strip()
	try:
		return int(maze_type)
	except:
		input("Type must be a number. (press enter to try again ctrl + c to end)")
		return find_type()

def upload():
	upload_file = input("Choose a file to upload: ").strip()
	try:
		return open_and_build(upload_file)
	except:
		input("File Not found. (press enter to try again ctrl + c to end)")
		return upload()

def build_new():
	maze_info = input("Enter maze height and width: ").strip()
	try:
		m = [int(i) for i in maze_info.split(" ")]
	except:
		input("Try again (Both hieght and with must be numbers: height width) (press enter to try again ctrl + c to end)")
		return build_new()
	while True:
		point_placement = input("Where would you like your start and end points to be placed in the maze? \n  1) Top and bottom \n  2) Left and Right \n  3) Random Placement \n").strip()
		try:
			if int(point_placement) == 1:
				maze_type = "h"
				break
			elif int(point_placement) == 2:
				maze_type = "v"
				break
			elif int(point_placement) == 3:
				maze_type = "r"
				break
			else:
				input("Try again using 1, 2, or 3 (press enter to try again ctrl + c to end)")
		except:
			input("Must be the number 1, 2 or 3 (press enter to try again ctrl + c to end)")
	maze = Maze()
	maze.build_new(m[0], m[1], maze_type)
	return maze
	

def save_file(file_name):
	with open(file_name, "w") as file:
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

m_type = find_type()
while True:
	if (m_type == 1):
		maze = build_new()
		break
	elif (m_type == 2):
		maze = upload()
		break
	else:
		input("Choose 1 or 2. (press enter to try again ctrl + c to end)")
		m_type = find_type()

maze.view_layout()
runner = Runner(maze)
runner.make_node_paths()
complete = "Yes" if runner.completed else "No"
print(f"Is maze possible? {complete}")

if runner.completed:	
	runner.build_path()
	runner.view_completed()
	file = input("What would you like to name this '.txt' file? \nFor default (completed.txt) press enter. ").strip()
	if re.match(r"^[\w\-. ]+$", file):
		save_file(f"{file}.txt")
	else:
		save_file("completed.txt")
	