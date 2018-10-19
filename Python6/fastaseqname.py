#!/usr/bin/env python3
import sys
import re

infile = open('Python_07.fasta','r')
outfile = open('Python_07_gname.txt','w')

for line in infile:
  seqname = re.search(r">.*?\s", line)
  if seqname:  
    found = seqname.group()
    outfile.write(found+'\n')
   #print(found)
  else: continue


