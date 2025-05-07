#!/usr/bin/python3


a = [2, 8, 9, 48, 8, 22, -12, 2]
b = [x + 2 for x in a]
c = [x for x in b if x >5]
d = set(c)
print (d)
