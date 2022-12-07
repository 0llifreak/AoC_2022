#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 7
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle
from anytree import Node, RenderTree, search, Walker, PreOrderIter, Resolver

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=7)
terminal = puzzle.input_data.split("\n")  # convert string to list

# AoC Example data
# ------------------------------------------------------------------

# terminal = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"""
# terminal = terminal.split("\n")

# ------------------------------------------------------------------

# --------------------------------
# Solution Part 1
# --------------------------------

root = Node("root", size=0)
parent_node = root
dirs = {}

for cmd in terminal:
    cmd = cmd.split(" ")
    # Generate directory node
    if cmd[0] == "dir":
        dir = Node(cmd[1], parent=parent_node, size=0)
        dirs[cmd[1]] = dir  # save directory name and node for later reference
    # Change parent node
    elif cmd[0] == "$":
        if cmd[1] == "cd":
            if cmd[2] == "/":
                parent_node = root
            elif cmd[2] == "..":
                parent_node = dir.parent
            else:
                new_dir = f"{cmd[2]}"
                parent_node = dirs[new_dir]
    # Generate file node
    else:
        file_name = cmd[1]
        file_size = int(cmd[0])
        Node(file_name, parent=parent_node, size=file_size)

# Print graph in terminal
# print(RenderTree(root).by_attr())

dir_size = []
solution2_dir = []
for dir in search.findall_by_attr(root, 0, "size"):
    size = 0
    for elem in [node for node in PreOrderIter(dir)]:
        size += elem.size
    solution2_dir.append(size)
    if size < 100000:
        dir_size.append(size)

# print("Solution Size;", dir_size)
print("Solution 1:", sum(dir_size))
# 1306611 is right :)

# --------------------------------
# Solution Part 2
# --------------------------------

# NOT WORKING!!!!

used_space = sum([node.size for node in PreOrderIter(root)])
free_space = 70000000 - used_space
print("free space:", free_space)
print("used space:", used_space)
print("needed space:", 30000000 - free_space)
# print(solution2_dir)
good_dirs = []
for dir in solution2_dir:
    # print(dir)
    if dir >= (30000000 - free_space):
        good_dirs.append(int(dir))

print(good_dirs)
print("Solution 2:", min(good_dirs))

# 26118278 too high
# 13371921 too high

# 10822529 lowest possible value
