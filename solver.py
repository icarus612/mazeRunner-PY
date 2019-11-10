from maze import Maze
from runner import Runner
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
	mazetype = input("Would you like to upload a maze or build a new one? \n  1) Build New \n  2) Upload \n")
	try:
		return int(mazetype)
	except:
		input("Type must be a number. (press enter to try again ctrl + c to end)")
		return find_type()

def upload():
	upload_file = input("Choose a file to upload: ")
	try:
		return open_and_build(upload_file)
	except:
		input("File Not found. (press enter to try again ctrl + c to end)")
		return upload()

def build_new():
	maze_info = input("Enter maze height and width: ")
	try:
		m = [int(i) for i in maze_info.split(" ")]
		maze = Maze()
		maze.build_new(m[0], m[1])
		return maze
	except:
		input("Try again (Both hieght and with must be numbers: height width) (press enter to try again ctrl + c to end)")
		return build_new()

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
	file = input("What would you like to name this '.txt' file? \nFor default (completed.txt) press enter. ")
	if re.match(r"^[\w\-. ]+$", file):
		save_file(f"{file}.txt")
	else:
		save_file("completed.txt")
	