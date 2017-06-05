#!/usr/bin/python
# Filename : excited_state.py
import os
import sys
import os.path
total=''
for dirpath, dirnames, filenames in os.walk('.'):
    for f in filenames:
        if os.path.splitext(f)[1]=='.log':
            myfile = open (f)
            lines = myfile.readlines()
            flen = len (lines)
            result = os.path.split(f)[1][:-11]+' '
            for i in range(flen):
                if 'eV' in lines[i]:
                    # print lines[i]
                    list = lines[i].split()
                    list2= list[8].split('=')
                    str = list[4]+' '+ list2[1] + ' '
                    result = result + str 
                else:
                    continue
            total = total +result+'\n'
print total
output = open ('ex_properties','w')
output.write(total)
output.close
