#!/usr/bin/env python3

import sys
import re

with open('Python_07_ApoI.fasta', 'r') as sequence:  #open this sequence and call it sequence
  for line in sequence:  #opens line by line
    line = line.rstrip() #removes new line commands
    
    for found in re.finditer(r'[GA]AATT[CT]', line): #finditer finds sequence and keeps location info 
      start = found.start() - 3  # hopefully starts from 1 because of >seq1
      end = found.end() - 3  
      print('An ApoI site starts at '+str(start)+' and ends at '+str(end)+'.') 
