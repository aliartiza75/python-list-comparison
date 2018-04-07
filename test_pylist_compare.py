#!/usr/bin/python3
###################################################################################################
# Name: python-list-comparision.py
# Summary: File code for python list comparision
# Author(s): Irtiza Ali
# LastUpdated: 12/01/2018
####################################################################################################

import copy

def compare_list(list1, list2):
    '''
    It will compare two python lists and return boolean result
    '''
    lis1 = copy.deepcopy(list1)
    lis2 = copy.deepcopy(list2)
    if len(lis2) != len(lis1):
        return False
    for val in lis2:
        if val in lis1:
            lis1.remove(val)
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

