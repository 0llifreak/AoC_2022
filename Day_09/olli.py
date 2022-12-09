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
import itertools

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=9)

# --------------------------------
# Solution Part 1
# --------------------------------

motions = puzzle.input_data.split("\n")

# motions = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""
# motions = motions.split("\n")

# motions = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20"""
# motions = motions.split("\n")


def tail_movement(head_position, tail_position, positions=[]):
    head_h = int(head_position[0])
    head_v = int(head_position[1])
    tail_h = int(tail_position[0])
    tail_v = int(tail_position[1])

    # Tail movement
    if (abs(head_h - tail_h) + abs(head_v - tail_v)) >= 3:
        if head_h - tail_h >= 1 and head_v - tail_v >= 1:
            tail_position += np.array([1, 1])
        elif head_h - tail_h >= 1 and head_v - tail_v <= -1:
            tail_position += np.array([1, -1])
        elif head_h - tail_h <= -1 and head_v - tail_v >= 1:
            tail_position += np.array([-1, 1])
        elif head_h - tail_h <= -1 and head_v - tail_v <= -1:
            tail_position += np.array([-1, -1])

    elif (head_v - tail_v) > 1:
        # move up
        tail_position += np.array([0, 1])
    elif (head_v - tail_v) < -1:
        # move down
        tail_position += np.array([0, -1])
    elif (head_h - tail_h) > 1:
        # move right
        tail_position += np.array([1, 0])
    elif (head_h - tail_h) < -1:
        # move left
        tail_position += np.array([-1, 0])

    positions.append(tail_position.copy().tolist())
    return tail_position


head_position = np.array([0, 0])  # horizontal, vertical
tail_position = np.array([0, 0])  # horizontal, vertical
rope_position = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10):
    rope_position[i] = np.array([0, 0])
positions = []
rope_tail_positions = []

for motion in motions:
    direction = motion.split(" ")[0]
    steps = int(motion.split(" ")[1])

    # Head movement
    if direction == "U":
        for _ in range(steps):
            head_position += np.array([0, 1])
            tail_position = tail_movement(head_position, tail_position, positions)
            # Part 2
            rope_position[0] += np.array([0, 1])
            for idx, position in enumerate(rope_position):
                if idx == len(rope_position) - 1:
                    break
                rope_tail = rope_position[idx + 1]
                rope_position[idx + 1] = tail_movement(position, rope_tail)
            rope_tail_positions.append(rope_position[-1].copy().tolist())

    elif direction == "D":
        for _ in range(steps):
            head_position += np.array([0, -1])
            tail_position = tail_movement(head_position, tail_position, positions)
            # Part 2
            rope_position[0] += np.array([0, -1])
            for idx, position in enumerate(rope_position):
                if idx == len(rope_position) - 1:
                    break
                rope_tail = rope_position[idx + 1]
                rope_position[idx + 1] = tail_movement(position, rope_tail)
            rope_tail_positions.append(rope_position[-1].copy().tolist())

    elif direction == "R":
        for _ in range(steps):
            head_position += np.array([1, 0])
            tail_position = tail_movement(head_position, tail_position, positions)
            # Part 2
            rope_position[0] += np.array([1, 0])
            for idx, position in enumerate(rope_position):
                if idx == len(rope_position) - 1:
                    break
                rope_tail = rope_position[idx + 1]
                rope_position[idx + 1] = tail_movement(position, rope_tail)
            rope_tail_positions.append(rope_position[-1].copy().tolist())

    elif direction == "L":
        for _ in range(steps):
            head_position += np.array([-1, 0])
            tail_position = tail_movement(head_position, tail_position, positions)
            # Part 2
            rope_position[0] += np.array([-1, 0])
            for idx, position in enumerate(rope_position):
                if idx == len(rope_position) - 1:
                    break
                rope_tail = rope_position[idx + 1]
                rope_position[idx + 1] = tail_movement(position, rope_tail)
            rope_tail_positions.append(rope_position[-1].copy().tolist())

positions.sort()  # remove duplicate positions
rope_tail_positions.sort()  # remove duplicate positions
print("Solution 1:", len(list(positions for positions, _ in itertools.groupby(positions))))  # remove duplicate positions
print(
    "Solution 2:", len(list(rope_tail_positions for rope_tail_positions, _ in itertools.groupby(rope_tail_positions)))
)  # remove duplicate positions
