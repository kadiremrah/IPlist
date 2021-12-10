#!/usr/bin/env python 
from fileinput import input
for y in sorted([x.strip().split('.')[::-1] for x in input()]): print '.'.join(y[::-1])
#usage sudo cat domains.txt | ./sort_domain.py > domains or python sort_domain.py dnsbl.conf.oisdfull > dnsbl.hosts
