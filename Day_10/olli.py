#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 10
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle
import numpy as np

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=10)

# --------------------------------
# Solution Part 1
# --------------------------------

signal = puzzle.input_data.split("\n")  # convert string to list


def calc_signal_strength():
    if cycle == 20:
        signal_strength.append(cycle * register_X)
    elif (cycle - 20) % 40 == 0:
        signal_strength.append(cycle * register_X)


register_X = 1
cycle = 0
signal_strength = []
for instruction in signal:
    instruction = instruction.split(" ")
    if instruction[0] == "noop":
        calc_signal_strength()
        cycle += 1
    elif instruction[0] == "addx":
        for _ in range(2):
            calc_signal_strength()
            cycle += 1
        register_X += int(instruction[1])

# print(signal_strength)
print("Solution 1:", sum(signal_strength))


# --------------------------------
# Solution Part 2
# --------------------------------


def check_vertical_position(cycle, vertical_position):
    if cycle % 40 == 0 and cycle != 0:
        vertical_position += 1
        cycle = 0
    return cycle, vertical_position


def draw_on_crt(crt, cycle, sprite_position, vertical_position):
    if ((sprite_position - 1) <= cycle) and (cycle <= (sprite_position + 1)):
        crt[vertical_position][cycle] = "X"
    else:
        crt[vertical_position][cycle] = "."
    cycle += 1
    cycle, vertical_position = check_vertical_position(cycle, vertical_position)
    return crt, cycle, sprite_position, vertical_position


# Init, scale and fill the np.array to display the letters on the CRT
np.set_printoptions(linewidth=200)
crt = np.zeros([6, 40], dtype=str)
crt.fill(" ")

sprite_position = 1
cycle = 0
vertical_position = 0
for instruction in signal:
    instruction = instruction.split(" ")
    if instruction[0] == "noop":
        crt, cycle, sprite_position, vertical_position = draw_on_crt(crt, cycle, sprite_position, vertical_position)
    elif instruction[0] == "addx":
        for _ in range(2):
            crt, cycle, sprite_position, vertical_position = draw_on_crt(crt, cycle, sprite_position, vertical_position)
        sprite_position += int(instruction[1])

print("Solution 2:")
print(crt)
