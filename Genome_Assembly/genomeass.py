#!/usr/bin/env python3

import re
from Bio import SeqIO


tigcount = 0
seqlen = 0
tiglist = []

for seq_record in SeqIO.parse('ecoliPB-filtered_0.50.contigs.fasta','fasta'):

  #print('ID',seq_record.id)
  
  tigcount = tigcount + 1
  
  seq = str(seq_record.seq) #gets the actual sequence

  #seqlen += len(seq) #length of sequence and adds the next sequence iteratively
  
  seqlen = len(seq)
  
  tiglist.append(seqlen)

longest = max(tiglist)
shortest = min(tiglist)

sortedlist = sorted(tiglist,reverse=True) 

genomehalf = sum(tiglist) / 2

for sortedlist 


print('The longest contig is', longest,'and the shortest contig is', shortest)
print(genomehalf)
print(sortedlist)
print(tiglist)
  
print(tigcount)

 







