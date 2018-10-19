#!/usr/bin/env python3
import sys

infile  = open('Python_06.txt', 'r')
outfile = open('Python_06uc.txt', 'w')

for line in infile:  #read line by line
  line = line.rstrip()
  line_lc= line.upper()
  #print(line_lc)
  outfile.write(line_lc,"\n")
