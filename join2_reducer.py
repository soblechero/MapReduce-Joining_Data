#!/usr/bin/env python
# coding=utf-8
import sys

last_key      = None
running_total = 0
abc_found     = False

#El input es el output de la función map: lista de <key \t value> sin espacios.
for line in sys.stdin:
    key, value = line.strip().split("\t")
    
    if 'ABC' == value: 
        abc_found = True

    if last_key != key:
        if abc_found:
            print('{0} {1}'.format(last_key, running_total))
            abc_found = False
        if value.isdigit():
            running_total = int(value)
        last_key = key
    else:
        if value.isdigit(): 
            running_total += int(value)
