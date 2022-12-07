#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2022 ---------
#
# Puzzle 7
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle
from anytree import Node, RenderTree, search, Walker, PreOrderIter, Resolver

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2022, day=7)
# --------------------------------
# Solution Part 1
# --------------------------------


terminal = puzzle.input_data.split("\n")  # convert string to list


# terminal = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"""
# ------------------------------------------------------------------
# terminal = """$ cd /
# $ ls
# dir btsgrbd
# 3868 cprq.fmm
# dir gcbpcf
# dir hfm
# 324644 lthcng.gnf
# 133181 nblfzrb.mrr
# 140568 sfrbjmmh.jnj
# dir tfsh
# dir vlsqgrw
# 202279 vmpgqbcd
# $ cd btsgrbd
# $ ls
# dir cmfdm
# dir cqd
# dir gvwvs
# dir nblfzrb
# dir nfm
# 293979 qwnml.bqn
# 159220 sdwnsgwv.mjm
# 327978 vzgwwjq.zbp
# 155479 zvspnvfr.zbc
# $ cd cmfdm
# $ ls
# dir gldnjj
# dir vhf
# $ cd gldnjj
# $ ls
# dir dvght
# 93750 lwvtzd.pws
# 176529 sdwnsgwv.mjm
# 100111 vmpgqbcd
# $ cd dvght
# $ ls
# dir tfbzq
# $ cd tfbzq
# $ ls
# 276592 tcghw.srg
# $ cd ..
# $ cd ..
# $ cd ..
# $ cd vhf
# $ ls
# 240217 hfm.rfp
# dir nblfzrb
# $ cd nblfzrb
# $ ls
# 160378 jhc
# $ cd ..
# $ cd ..
# $ cd ..
# $ cd cqd
# $ ls
# 305358 bnddfgrb
# dir dwqncqp
# dir hnnfdtbh
# dir jhc
# dir nblfzrb
# 327762 scnm.qbf
# 165080 vmpgqbcd
# 190041 vzgwwjq.zbp
# dir zwv
# $ cd dwqncqp
# $ ls
# 122570 slpgmhv
# 278461 zlnbcwr
# $ cd ..
# $ cd hnnfdtbh
# $ ls
# 334830 gfprhn.rjj
# $ cd ..
# $ cd jhc
# $ ls
# 179593 fgb.btb
# $ cd ..
# $ cd nblfzrb
# $ ls
# dir clbcgvhc
# dir jhc
# dir lsrnz
# dir mctd
# $ cd clbcgvhc
# $ ls
# 285825 hnn
# 238272 nblfzrb.wvr
# $ cd ..
# $ cd jhc
# $ ls
# 99731 nblfzrb.svz"""
# terminal = terminal.split("\n")

root = Node("root")
parent_node = root
insert = False
dirs = {}
for cmd in terminal:
    # print(cmd)
    cmd = cmd.split(" ")
    if cmd[0] == "dir" and insert == True:
        # print("dir:", cmd[1])
        dir = Node(cmd[1], parent=parent_node, size=0)
        dirs[cmd[1]] = dir
    elif cmd[0] == "$":
        # print(cmd)
        if cmd[1] == "cd":
            if cmd[2] == "/":
                parent_node = root
            elif cmd[2] == "..":
                parent_node = dir.parent
                # print(dir)
            else:
                # parent_node = search.findall_by_attr(root, cmd[2], name="name")[-1]
                # parent_node = dir
                # print(parent_node)
                dings = f"{cmd[2]}"
                parent_node = dirs[dings]
                # print(parent_node)

            insert = False
        elif cmd[1] == "ls":
            insert = True
    else:
        # print("data:", cmd[1], cmd[0])
        file_name = cmd[1]
        file_size = int(cmd[0])
        Node(file_name, parent=parent_node, size=file_size)

# for pre, _, node in RenderTree(root):
#     print("%s%s" % (pre, node.name))

print(RenderTree(root).by_attr())
# print(search.findall_by_attr(root, 0, "size"))

dir_size = []
solution_dir = []
for dir in search.findall_by_attr(root, 0, "size"):
    size = 0
    # print(dir)
    for elem in [node for node in PreOrderIter(dir)]:
        # print(elem)
        size += elem.size
    # print("--------------------------------------------------------------------")
    if size < 100000:
        dir_size.append(size)

# print("Solution Size;", dir_size)
print("Solution:", sum(dir_size))

# 1315951 too high

# 1031698 too low
