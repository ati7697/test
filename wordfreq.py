#!/usr/bin/python3

import sys
import string
f = open("test.txt", "r")
words = f.read().split()
d = dict()
for word in words:
	t = word.translate(str.maketrans('','',string.punctuation)).upper()
	if(len(t) > 0):
		d[t] = d.get(t,0) + 1

l = list()
for key,value in d.items():
	l.append((value,key))

l = sorted(l, reverse=True)


