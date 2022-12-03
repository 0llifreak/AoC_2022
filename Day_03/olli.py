#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 3
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle


# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=3)

# --------------------------------
# Solution Part 1
# --------------------------------

rucksack = puzzle.input_data.split("\n")  # convert string to list

elem_sum = 0
for compartment in rucksack:
    length = len(compartment)
    first_compartment = compartment[: int(length / 2)]
    second_compartment = compartment[int(length / 2) :]
    item = set(first_compartment).intersection(second_compartment)
    elem = item.pop()
    if elem.islower():
        elem_sum += ord(elem) - 96
    else:
        elem_sum += ord(elem) - 38

print("Solution Part 1:", elem_sum)

# --------------------------------
# Solution Part 2
# --------------------------------

elem_sum = 0
three_elves = []
for compartment in rucksack:
    three_elves.append(compartment)
    if len(three_elves) == 3:
        first_compartment = three_elves[0]
        second_compartment = three_elves[1]
        third_compartment = three_elves[2]
        item = set(set(first_compartment).intersection(second_compartment).intersection(third_compartment))
        elem = item.pop()
        if elem.islower():
            elem_sum += ord(elem) - 96
        else:
            elem_sum += ord(elem) - 38
        three_elves.clear()

print("Solution Part 2:", elem_sum)
