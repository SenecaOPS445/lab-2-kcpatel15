#!/usr/bin/env python3

#Author: Keval Patel
#Author ID: kcpatel15@myseneca.ca
#Date Created: 2024/05/23

import sys

import sys

if len(sys.argv) > 1:
  timer = int(sys.argv[1])
else:
  timer = 3

while timer > 0:
  print(timer)
  timer = timer - 1

print("blast off!")