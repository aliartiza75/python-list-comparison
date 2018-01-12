#!/usr/bin/python3
###################################################################################################
# Name: python-list-comparision.py
# Summary: File code for python list comparision
# Author(s): Irtiza Ali
# LastUpdated: 12/01/2018
####################################################################################################

def compare_list(lis1, lis2):
    '''
    It will compare two lists
    '''
    if len(lis1) != len(lis2):
        return False
    for val in lis1:
        if val in lis2:
            lis2.remove(val)
        else:
            return False
    return True

# Tests
lis1 = [1,2,3]
lis2 = [2,1]

print(compare_list(lis1, lis2))

lis1 = [1,2,3]
lis2 = [2,1,"3"]

print(compare_list(lis1, lis2))

lis1 = ['1','2','3']
lis2 = ['2','1']

print(compare_list(lis1, lis2))


lis1 = [1,2,3]
lis2 = [2,1,3]

print(compare_list(lis1, lis2))

lis1 = [{1:1,2:2}]
lis2 = [{1:1,2:2}]

print(compare_list(lis1, lis2))


