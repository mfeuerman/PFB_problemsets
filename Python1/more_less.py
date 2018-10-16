#!/usr/bin/env python3
import sys

count =  int(sys.argv[1]) 
if count < 18:
  message = 'is less than 18'
  print (count, message)
elif count > 18:
  message = 'is greater than 18'
  print (count, message)
else:
  message = 'must be equal to 18'
  print (count, message)

