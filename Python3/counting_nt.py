#!/usr/bin/env python3
import sys

dna = sys.argv[1]
numA = dna.count('A') #counting As
numa = dna.count('a') #counting as
numAanda = int(numA) + int(numa)
print("There are", (numAanda), "A(s) and a(s) in the this sequence")

numT = dna.count('T') #counting Ts
numt = dna.count('t') #counting ts
numTandt = int(numT) + int(numt)
print("There are", (numTandt), "T(s) and t(s)  in the this sequence")

numG = dna.count('G') #counting Gs
numg = dna.count('g') #counting gs
numGandg = int(numG) + int(numg)
print("There are", (numGandg), "G(s) and g(s)  in the this sequence")

numC = dna.count('C')
numc = dna.count('c')
numCandc = int(numC) + int(numc)
print("There are", (numCandc), "C(s) and c(s) in the this sequence")
