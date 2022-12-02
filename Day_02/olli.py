#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 2
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=2)

# --------------------------------
# Solution Part 1
# --------------------------------

# Opponent:
# A = Rock
# B = Paper
# C = Scissor

# Me:
# X = Rock
# Y = Paper
# Z = Scissor

rps = puzzle.input_data.split("\n")  # convert string to list
score = 0
for round in rps:
    opponent = round[0]
    me = round[2]
    # Calculate personal score
    if me == "X":
        score += 1
    elif me == "Y":
        score += 2
    elif me == "Z":
        score += 3
    # print(opponent, me)

    # Calculate game score
    # Rock defeats Scissors
    if me == "X" and opponent == "C":
        score += 6
    elif me == "Z" and opponent == "A":
        score += 0
    # Scissors defeats Paper
    elif me == "Z" and opponent == "B":
        score += 6
    elif me == "Y" and opponent == "C":
        score += 0
    # Paper defeats Rock
    elif me == "Y" and opponent == "A":
        score += 6
    elif me == "X" and opponent == "B":
        score += 0
    # Draw
    else:
        score += 3

print("Score", score)
