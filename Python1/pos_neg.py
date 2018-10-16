#!/usr/bin/env python3
import sys

# test for positive or negative number

number = int(sys.argv[1])

if number < 0:
  message = 'negative'
  print(number, message)

elif number > 0:
  message =' positive'
  print(number, message)

  if number < 50:
    message = 'wow less than 50'
    print(number, message)

    if number % 2 == 1:
      message = 'number is odd'
      print (message)

    elif number % 2  == 0:
      message = 'number is smaller than 50 and even'
      print (message) 

  elif number > 50:
    if number % 3 == 0:
      message = 'number is greater than 50 and divisible by 3'
      print (message)

else:
  message = 'must be zero'
  print(number, message)
