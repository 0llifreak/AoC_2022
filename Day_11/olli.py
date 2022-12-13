#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 11
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle
import numpy as np

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=11)

# --------------------------------
# Solution Part 1 & 2
# --------------------------------

notes = puzzle.input_data.split("\n")  # convert string to list
# Remove leading whitespaces
my_notes = [line.lstrip() for line in notes]


class Monkey:
    def __init__(self, name, items, operation, quotient, if_true, if_false, inspected):
        self.name = name
        self.items = items
        self.operation = operation
        self.quotient = quotient
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = inspected

    def process(self, item, rounds):
        old = int(item)
        if rounds == 20:
            worry = eval(self.operation) % 9699690 // 3
        else:
            worry = eval(self.operation) % 9699690

        if worry % self.quotient == 0:
            monkey_list[self.if_true].items.append(worry)
        else:
            monkey_list[self.if_false].items.append(worry)
        self.inspected += 1

    def __str__(self):
        return f"""Name: {self.name} \nItems: {self.items} \nOperation: {self.operation} \nQuotient: {self.quotient} \nIf True: {self.if_true} \nIf False: {self.if_false} \nInspected: {self.inspected}"""


def generate_monkeys():
    monkey_list = []
    for line in my_notes:
        note = line.split(": ")
        if note[0].split(" ")[0] == "Monkey":
            name = note[0][:-1]
        elif note[0] == "Starting items":
            item_list = [int(x) for x in note[1].split(", ")]  # convert string to int
        elif note[0] == "Operation":
            operation = note[1].split("= ")[1]
        elif note[0] == "Test":
            quotient = int(note[1].split(" ")[-1])
        elif note[0] == "If true":
            true_monkey = int(note[1].split(" ")[-1])
        elif note[0] == "If false":
            false_monkey = int(note[1].split(" ")[-1])

            monkey_list.append(Monkey(name, item_list, operation, quotient, true_monkey, false_monkey, 0))
    return monkey_list


ROUNDS = [20, 10000]  # Part 1, Part 2
for n in ROUNDS:
    monkey_list = generate_monkeys()
    for _ in range(n):
        for monkey in monkey_list:
            while monkey.items:
                monkey.process(monkey.items.pop(0), n)

    inspected_list = []
    for monkey in monkey_list:
        inspected_list.append(monkey.inspected)
    inspected_list.sort(reverse=True)  # sort from max to min

    if n == 20:
        print("Solution 1:", inspected_list[0] * inspected_list[1])
    else:
        print("Solution 2:", inspected_list[0] * inspected_list[1])
