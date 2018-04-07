#!/usr/bin/python3
###################################################################################################
# Name: listcompare.py
# Summary: File code for python list comparision
# Author(s): Irtiza Ali
# LastUpdated: 08/04/2018
####################################################################################################

def compare_list(list1, list2):
    '''
    It will compare two python lists and return boolean result
    '''
    if len(list2) != len(list1):
        return False
    for val in list2:
        if val not in list1:
            return False
    return True
