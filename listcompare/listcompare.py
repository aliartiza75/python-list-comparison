#!/usr/bin/python3
###################################################################################################
# Name: listcompare.py
# Summary: File code for python list comparision
# Author(s): Irtiza Ali
# LastUpdated: 09/04/2019
####################################################################################################


def compare_list(list1, list2):
    '''
    It will compare two python lists and return boolean result
    '''

    if isinstance(list1, list) and isinstance(list2, list):

        if len(list2) != len(list1):
            return False
        # check item of list2 exists in list1
        for list2_item in list2:
            if list2_item not in list1:
                return False
        # check item of list1 exists in list2
        for list1_item in list1:
            if list1_item not in list2:
                return False
        return True
    raise Exception("Invalid Data provided")
