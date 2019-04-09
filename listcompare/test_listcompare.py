#!/usr/bin/python3
###################################################################################################
# Name: test_listcompare.py
# Summary: File contains tests for the pylistcompare file
# Author(s): Irtiza Ali
# LastUpdated: 08/04/2018
####################################################################################################
import unittest
import listcompare


class TestSum(unittest.TestCase):
    def setUp(self):
        self.compare_list = listcompare.compare_list

    def test_negative_compare_int_lists(self):
        lis1 = [1, 2, 3]
        lis2 = [2, 1]
        self.assertFalse(self.compare_list(lis1, lis2))

    def test_positive_compare_int_lists_(self):
        lis1 = [2, 1, 3]
        lis2 = [1, 2, 3]
        self.assertTrue(self.compare_list(lis1, lis2))

    def test_negative_compare_int_and_multi_data_type_lists(self):
        lis1 = [1, 2, 3]
        lis2 = [2, 1, "3"]
        self.assertFalse(self.compare_list(lis1, lis2))

    def test_negative_compare_str_lists(self):
        lis1 = ['1', '2', '3']
        lis2 = ['2', '1']

        self.assertFalse(self.compare_list(lis1, lis2))

    def test_positive_compare_dict_lists(self):
        lis1 = [{1: 1, 2: 2}]
        lis2 = [{2: 2, 1: 1}]

        self.assertTrue(self.compare_list(lis1, lis2))

    def test_negative_compare_invalid_types(self):
        lis1 = {}
        lis2 = 1

        self.assertRaises(Exception, self.compare_list, lis1, lis2)

    def test_positive_compare_list_complex_types(self):
        lis1 = [1, "a", {1: 1, 2: 2}, 3]
        lis2 = [3, 1, {1: 1, 2: 2}, "a"]

        self.assertTrue(self.compare_list(lis1, lis2))


if __name__ == '__main__':
    unittest.main()
