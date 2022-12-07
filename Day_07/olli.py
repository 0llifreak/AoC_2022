#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 7
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=7)
# --------------------------------
# Solution Part 1
# --------------------------------


terminal = puzzle.input_data.split("\n")  # convert string to list
# print([{"a": {"b.txt:14848412", "c.dat: 8540451"}}][0])

terminal = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
terminal = terminal.split("\n")

directories = []
for cmd in terminal:
    print(cmd)
    if cmd[0] == "$":
        print("command")
    elif cmd[:3] == "dir":
        print("directorie")
    else:
        print("data")
        print(cmd.split(" "))
