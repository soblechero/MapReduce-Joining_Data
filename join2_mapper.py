#!/usr/bin/env python
# coding=utf-8
import sys

#El input es un fichero con lineas <key,value> sin espacios
for line in sys.stdin:
    key, value = line.strip().split(",")
    
    if value == 'ABC' or value.isdigit():
        print( '%s\t%s' % (key, value) )