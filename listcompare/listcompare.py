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
        return True
    raise Exception("Invalid Data provided")

def parse_nested_list(list1):
    '''
    It will parse the nest list and store the data in a dictionary. 


    Example:

    l1 =  [1, 2, "a", {"key": "value"}, ["a", "b", 1], (1, 2)]
   

    dict1 = {
        "int": {
            "1": [1, 2],
            "2"" [1]
        },

        "str": {
            "1": ["a"]
            "2": ["a", "b"]
        },


        "tuple": {
           "1": [(1, 2)]

        },

        "dict": {
          "1": [{"key": "value"}]
        }
    }

    '''
    parsed_list = []
    return parsed_list
