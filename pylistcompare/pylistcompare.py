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
