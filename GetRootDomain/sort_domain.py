#!/usr/bin/env python 
from fileinput import input
for y in sorted([x.strip().split('.')[::-1] for x in input()]): print '.'.join(y[::-1])
# to sort your file  "sample.txt" on linux terminal command : python sort_domain.py sample.txt > output.txt
# this will sort file lines in reverse order so you will get list of lines sorted by same root.domains
