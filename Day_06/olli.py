#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 6
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=6)

# --------------------------------
# Solution Part 1
# --------------------------------

signal = puzzle.input_data.split("\n")[0]  # convert string to list

marker = []
for idx, char in enumerate(signal):
    marker.append(char)
    if len(marker) == 4:
        if len(set(marker)) == 4:
            break
        marker.pop(0)

print("Solution 1:", idx + 1)

# --------------------------------
# Solution Part 2
# --------------------------------

marker = []
for idx, char in enumerate(signal):
    marker.append(char)
    if len(marker) == 14:
        if len(set(marker)) == 14:
            break
        marker.pop(0)

print("Solution 2:", idx + 1)
