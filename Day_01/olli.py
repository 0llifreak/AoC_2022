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
sum_calories = 0
for calorie in calories:
    if calorie == "":
        elves.append(sum_calories)
        sum_calories = 0
    else:
        sum_calories += int(calorie)
print(max(elves))

# --------------------------------
# Solution Part 2
# --------------------------------

top3_sum = sum(sorted(elves, reverse=True)[:3])
print(top3_sum)
