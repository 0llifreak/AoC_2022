#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 8
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=8)

# --------------------------------
# Solution Part 1
# --------------------------------

forest = puzzle.input_data.split("\n")

visible_trees = set()
row_len = len(forest[0])

for i, row in enumerate(forest):
    col = [line[i] for line in forest]
    visible_trees_horizontal = [((i, 0), row[0])]
    visible_trees_vertical = [((0, i), col[0])]
    # From left to right
    for k, tree in enumerate(row):
        if tree > visible_trees_horizontal[-1][1]:
            visible_trees_horizontal.append(((i, k), tree))
    # From right to left
    visible_trees_horizontal.append(((i, row_len - 1), row[-1]))
    for k, tree in enumerate(row[::-1]):
        if tree > visible_trees_horizontal[-1][1]:
            visible_trees_horizontal.append(((i, row_len - k - 1), tree))
    # From top to btm
    for k, tree in enumerate(col):
        if tree > visible_trees_vertical[-1][1]:
            visible_trees_vertical.append(((k, i), tree))
    # From btm to top
    visible_trees_vertical.append(((row_len - 1, i), col[-1]))
    for k, tree in enumerate(col[::-1]):
        if tree > visible_trees_vertical[-1][1]:
            visible_trees_vertical.append(((row_len - k - 1, i), tree))
    visible_trees = visible_trees | set(visible_trees_horizontal) | set(visible_trees_vertical)

print("Solution 1:", len(visible_trees))


# --------------------------------
# Solution Part 2
# --------------------------------

max_scenic_score = -1
for i in range(1, len(forest) - 1):
    for k in range(1, len(forest[0]) - 1):
        tree = forest[i][k]
        scenic_score = [0, 0, 0, 0]

        # Look left
        for n in range(1, i + 1):
            scenic_score[0] += 1
            if tree <= forest[i - n][k]:
                break
        # Look right
        for n in range(i + 1, len(forest)):
            scenic_score[1] += 1
            if tree <= forest[n][k]:
                break
        # Look up
        for n in range(1, k + 1):
            scenic_score[2] += 1
            if tree <= forest[i][k - n]:
                break
        # Look down
        for n in range(k + 1, len(forest[0])):
            scenic_score[3] += 1
            if tree <= forest[i][n]:
                break

        score = scenic_score[0] * scenic_score[1] * scenic_score[2] * scenic_score[3]
        if score > max_scenic_score:
            max_scenic_score = score

print("Solution 2:", max_scenic_score)
