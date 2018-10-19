#!/usr/bin/env python3
import sys
import re

infile = open('Python_07.fasta','r')
outfile = open('Python_header.txt','w')

for line in infile:
  line = line.rstrip()  

  fastahead = re.search(r">(.*?)\s(.*)$", line)
  if fastahead:  
    ID = fastahead.group(1)
    Des = fastahead.group(2)
    #outfile.write(found+'\n')
    print("ID is",ID, "and description of the sequence is", Des)
  else: continue


