#!/usr/bin/env python3
import sys
import re

with open('Python_07_nobody.txt','r') as nobody: #open file and define as nobody

  for line in nobody: 
    for found in re.finditer(r'Nobody', line):  #finditer keeps location information
      start = found.start() + 1     #start from 1
      end = found.end() + 1  #correct for starting from 1
      print('Nobody starts at '+str(start)+' and ends at '+str(end)+'.') 


