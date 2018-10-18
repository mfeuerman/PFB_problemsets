#!/usr/bin/env python3
import sys

favdict = {'redwine':"pinot noir",' whitewine':"chardonnay", 'spirit':"whiskey"}
print(favdict)

print(favdict['spirit'])

fav_spirit = 'spirit'
print(favdict[fav_spirit])

favdict[fav_spirit] = "tequila"
print(favdict)

for drinks in favdict:
  bev = favdict[drinks]
  print(drinks)

userinput = input("What can I get you")
print(favdict[userinput])
