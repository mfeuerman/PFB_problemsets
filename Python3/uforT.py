#!/usr/bin/env python3
import sys
#this will search a sequence for Ts and replace them with Us
dna = sys.argv[1]
dnaT = dna.replace('t','T')
dnaU = dnaT.replace('T','U')
print(dnaU)
