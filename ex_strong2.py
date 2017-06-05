#!/usr/bin/python/
#Filename : ex_strong.py
def ex_strong(lines):
    list = lines.split(' ')
    #print list
    name = list [0]
    f=2
    num = 0
    result_total = ''
    for i in range (len(list)): 
        if float(list[f]) >= 0.01:
            num += 1
            if num > 2:
                break
            else:
                energy = list [f-1]
                strength = list [f]
                state = str(f/2)
                result = name +' '+ energy + ' ' + strength + ' ' +  state + ' '
                result_total +=result
                f+=2
        else:
            f+=2
        if f > 39:
            break 
    #print f
    print result_total       
myfile = open ('ex_properties')
lines = myfile.readlines()
flen = len (lines)
total = ''
for i in range (flen):
    result =ex_strong(lines[i])
    #total = total +result +'\n'
#print total

