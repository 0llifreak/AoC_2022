#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 4
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=4)

# --------------------------------
# Solution Part 1
# --------------------------------

sections = puzzle.input_data.split("\n")  # convert string to list
counter = 0


def get_range(pair):
    return list(range(int(pair.split("-")[0]), int(pair.split("-")[1]) + 1))


for pair in sections:
    pair = pair.split(",")
    first_list = get_range(pair[0])
    second_list = get_range(pair[1])
    if len(set(first_list + second_list)) == len(first_list) or len(set(first_list + second_list)) == len(second_list):
        counter += 1
print("Solution 1:", counter)
