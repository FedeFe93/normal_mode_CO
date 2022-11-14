#!/usr/bin/env python3

import re,os,glob,sys,shutil,subprocess
import pandas as pd
from pandas import DataFrame
import numpy as np
from itertools import islice

filename=sys.argv[1]     #xyz coordinates
max_value = [0, 0, 0]  # value, line, position
with open(filename, 'r') as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        if ' Frequencies -- ' in line and float(line.split()[2]) > 1430 and float(line.split()[2]) < 1800:     #range CO stretching
            line0=(lines[index])
            line=(lines[index+23])
            line_data = line.split()[2:]
            # check if element digit and bigger then max value - save it
            for el_index, element in enumerate(line_data):
                if element and abs(float(element)) > max_value[0]:
                    max_value = [abs(float(element)), index, el_index]
                    max_value2= el_index
                    max_value3= index
#print(max_value)
#print(max_value2)
a=(lines[max_value3])
if 0 <= int(max_value2) < 3:
    print(a.split()[2])
elif 3 <= int(max_value2) <6:
    print(a.split()[3])
elif int(max_value2)>= 6:
    print(a.split()[4])
