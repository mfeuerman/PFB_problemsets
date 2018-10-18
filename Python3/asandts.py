#!/usr/bin/env python3
import sys

#A-T content of a DNA sequence

dna = ('ATTTAAGGCCTTAGCTAGGGCC')
dnatot = len(dna) #Number of nucleotides
conA = dna.count('A') #Number of A
conT = dna.count('T') #Number of T
print("The length of the sequence is", dnatot, ", the number of As are", conA, ", the number of Ts are", conT)
print
# (int(conA) + int(conT))
