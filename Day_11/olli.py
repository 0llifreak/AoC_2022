#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 11
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=11)

# --------------------------------
# Solution Part X
# --------------------------------

notes = puzzle.input_data.split("\n")  # convert string to list

notes = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
notes = notes.split("\n")

# Remove leading whitespaces
my_notes = [line.lstrip() for line in notes]
# print(my_notes)


monkey_list = []
for line in my_notes:
    note = line.split(": ")
    # print(note)
    if note[0] == "Starting items":
        # print(note[1].split(", "))
        item_list = [int(x) for x in note[1].split(", ")]  # convert string to int
        monkey_list.append(item_list)


print(monkey_list)
