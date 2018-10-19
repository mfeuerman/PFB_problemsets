#!/usr/bin/env python3
import sys
import re

fileIn =  open('Python_07_nobody.txt','r') #open file and define as nobody
bigguy = open("Max.txt","w")
for line in fileIn: 
  for found in re.sub(r'Nobody','Max', line):  #what to find, what to put in, what you are working on
    bigguy.write(found)



