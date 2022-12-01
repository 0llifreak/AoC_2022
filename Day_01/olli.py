#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 1
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=1)

# --------------------------------
# Solution Part 1
# --------------------------------

calories = puzzle.input_data.split("\n")  # convert string to list
elves = []
sum = 0
for calorie in calories:
    if calorie == "":
        elves.append(sum)
        sum = 0
    else:
        sum += int(calorie)
print(max(elves))

# --------------------------------
# Solution Part 2
# --------------------------------

elves.sort(reverse=True)
top3_sum = elves[0] + elves[1] + elves[2]
print(top3_sum)
