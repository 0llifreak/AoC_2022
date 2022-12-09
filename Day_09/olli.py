#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 9
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle
import numpy as np

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=9)

# --------------------------------
# Solution Part 1
# --------------------------------

motions = puzzle.input_data.split("\n")

motions = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
motions = motions.split("\n")

# print(motions[0])
head_position = np.array([0, 0])  # horizontal, vertical

print(head_position)
for motion in motions:
    direction = motion.split(" ")[0]
    steps = int(motion.split(" ")[1])
    print(direction, steps)
    if direction == "U":
        for _ in range(steps):
            head_position += np.array([0, 1])
            print("UP")
    elif direction == "D":
        for _ in range(steps):
            head_position += np.array([0, -1])
            print("DOWN")
    elif direction == "R":
        for _ in range(steps):
            head_position += np.array([1, 0])
            print("RIGHT")
    elif direction == "L":
        for _ in range(steps):
            head_position += np.array([-1, 0])
            print("LEFT")
    print("head pos:", head_position)
