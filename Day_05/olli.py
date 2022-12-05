#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 5
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle
from itertools import chain

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=5)

# --------------------------------
# Solution Part 1
# --------------------------------


def remove_spaces(cargo_list):
    return [s for s in cargo_list if s != " "]


cargo = puzzle.input_data.split("\n")  # convert string to list

# Get cargo stacks
cargo_list = list(zip(*cargo[:8][::-1]))
cargo_dict = {
    "1": remove_spaces(cargo_list[1]),
    "2": remove_spaces(cargo_list[5]),
    "3": remove_spaces(cargo_list[9]),
    "4": remove_spaces(cargo_list[13]),
    "5": remove_spaces(cargo_list[17]),
    "6": remove_spaces(cargo_list[21]),
    "7": remove_spaces(cargo_list[25]),
    "8": remove_spaces(cargo_list[29]),
    "9": remove_spaces(cargo_list[33]),
}

# Get movement data
movements = cargo[10:]
for movement in movements:
    movement_list = movement.split(" ")
    for _ in range(int(movement_list[1])):
        cargo_dict[movement_list[5]].append(cargo_dict[movement_list[3]].pop())

solution = ""
for stack in cargo_dict.values():
    solution += stack[-1]
print("Solution 1:", solution)


# --------------------------------
# Solution Part 2
# --------------------------------

# Get cargo stacks
cargo_list = list(zip(*cargo[:8][::-1]))
cargo_dict = {
    "1": remove_spaces(cargo_list[1]),
    "2": remove_spaces(cargo_list[5]),
    "3": remove_spaces(cargo_list[9]),
    "4": remove_spaces(cargo_list[13]),
    "5": remove_spaces(cargo_list[17]),
    "6": remove_spaces(cargo_list[21]),
    "7": remove_spaces(cargo_list[25]),
    "8": remove_spaces(cargo_list[29]),
    "9": remove_spaces(cargo_list[33]),
}

# Get movement data
movements = cargo[10:]
for movement in movements:
    movement_list = movement.split(" ")
    crates = []
    for _ in range(int(movement_list[1])):
        crates.append(cargo_dict[movement_list[3]].pop())
    crates.reverse()
    cargo_dict[movement_list[5]].append(crates)
    cargo_dict[movement_list[5]] = list(chain(*cargo_dict[movement_list[5]]))  # flatten the nested list

solution2 = ""
for stack in cargo_dict.values():
    solution2 += stack[-1]
print("Solution 2:", solution2)
