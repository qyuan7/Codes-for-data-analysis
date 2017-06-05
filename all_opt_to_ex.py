#!/usr/bin/python
# Filename : all_opt_to_ex.py
def opt_to_ex(file):
    import os
    myfile = open (file)
    lines = myfile.readlines()
    flen = len(lines)
    orientation = ''
# get file name for gaussian output. NOTE:only local jobs rather than hpc jobs are suitable for this step.
    for i in range(flen):
        if '%chk=' in lines[i]:
            lines[i]= lines[i].strip('\n')
            if '/' in lines[i]:
                name_parts = lines[i].split('/')
            else:
                name_parts = lines[i].split('=')
            temp_name = name_parts[-1]
# number into atom change
    def number_to_atom(number):
        atom = 'none'
        if number == '6':
            atom = 'C'
        elif number == '8':
            atom = 'O'
        elif number == '1':
            atom = 'H'
        elif number == '17':
            atom = 'Cl'
        elif number == '16':
            atom = 'S'
        elif number == '7':
            atom = 'N'
        elif number == '9':
            atom = 'F'
        elif number == '35':
            atom = 'Br'
        return atom
# Search for converged geometries
    for i in range(flen):
        if 'Optimization completed' in lines[i]:
            while True:
                i+=1
                if 'Standard orientation:' in lines[i]:
                    break
            i+=4
            natm=0
            while True:
                i+=1
                if '--' in lines[i]:
                    break
                natm +=1
# Remove redundant numbers in output lines and save coordinates in coord
                parts = lines[i].split(' ')
                parts_extract = parts [7:24]+parts[32:]
                strc1 = ' '.join(parts_extract)
                strc2 = strc1.lstrip()
                parts_2 = strc2.split(' ')
                parts_2[0] = number_to_atom(parts_2[0])
                strc = ' '.join (parts_2)
                orientation +=  strc
    myfile.close()
    coord = open ( 'coord','w')
    coord.write(orientation)
    coord.close()
# Divide coord into gaussian input files
    myfile2 = open ('coord', 'r')
    lines = myfile2.readlines()
    flen = len(lines)
    input_name = temp_name[:-4]+'_ex.com'
    gaussian_input = open (input_name, 'w')
    gaussian_input.write ('%nprocshared=8\n%mem=63800MB \n')
    gaussian_input.write ('%chk='+input_name[:-4]+'.chk\n')
    gaussian_input.write ('# td=(nstates=20,root=1) b3lyp/6-311G(d,p)\n')
    gaussian_input.write ('\nTitle Card \n\n0 1\n')
    for i in range(flen):
        gaussian_input.write (lines[i])
        i+=1
    gaussian_input.write ('\n\n')
    gaussian_input.close()
    coord.close()
    os.remove('coord')
import sys
import os.path
total=''
for dirpath, dirnames, filenames in os.walk('.'):
    for f in filenames:
        if os.path.splitext(f)[1]=='.log':
            opt_to_ex(f)
        else:
            continue
