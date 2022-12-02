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

# --------------------------------
# Solution Part 2
# --------------------------------

# X = Lose
# Y = Draw
# Z = Win

score_2 = 0
for round in rps:
    opponent = round[0]
    strategy = round[2]

    # Calculate game score
    # Lose
    if strategy == "X":
        if opponent == "A":
            score_2 += 3
        elif opponent == "B":
            score_2 += 1
        elif opponent == "C":
            score_2 += 2
    # Draw
    elif strategy == "Y":
        if opponent == "A":
            score_2 += 4
        elif opponent == "B":
            score_2 += 5
        elif opponent == "C":
            score_2 += 6
    # Win
    elif strategy == "Z":
        if opponent == "A":
            score_2 += 8
        elif opponent == "B":
            score_2 += 9
        elif opponent == "C":
            score_2 += 7

print("Score 2", score_2)
