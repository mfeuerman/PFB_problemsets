#!/usr/bin/env python3

import sys
import re

#Take a multi-FASTA Python_08.fasta file from user input and calculate the nucleotide composition
# for each sequence. Use a datastructure to keep count.
# Print out each sequence name and its compostion in this format 
#seqName\tA_count\tT_count\tG_count\C_count


infile = sys.argv[1]  #file by user input
with open(infile r") as gene:
  header = ''
  sequence = ''
  sequences = {}
  for line in gene: #opens line by line
    line = line.rstrip() #removes new line commands
    
    if line.startswith('>'): #character at the beginning of the line
      if header != '':
        sequences[header]=sequences
      
      header = line.split()[0]
      
    else:
      sequence = sequence+line #adds the next line of sequence not header

    sequences.update(sequences)
    print(sequences)


#admin

