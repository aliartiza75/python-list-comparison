#!/usr/bin/python3
###################################################################################################
# Name: test_listcompare.py
# Summary: File contains tests for the pylistcompare file
# Author(s): Irtiza Ali
# LastUpdated: 08/04/2018
####################################################################################################
import listcompare as plc

# Tests
lis1 = [1,2,3]
lis2 = [2,1]

print(plc.compare_list(lis1, lis2))

lis1 = [1,2,3]
lis2 = [2,1,"3"]

print(plc.compare_list(lis1, lis2))

lis1 = ['1','2','3']
lis2 = ['2','1']

print(plc.compare_list(lis1, lis2))


lis1 = [1,2,3]
lis2 = [2,1,3]

print(plc.compare_list(lis1, lis2))

lis1 = [{1:1,2:2}]
lis2 = [{1:1,2:2}]

print(plc.compare_list(lis1, lis2))

lis1 = {}
lis2 = 1

print(plc.compare_list(lis1, lis2))

