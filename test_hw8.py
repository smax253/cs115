'''
Created on Oct 24, 2018
Last modified on Oct 24, 2018

@author: Scott Murray

Based on test_hw6.py by Brian Borowski

CS115 - Hw 8 Test Script
'''

import unittest
import hw8

class Test(unittest.TestCase):

    def test01(self):
        sequence = '0' * 64
        self.assertEqual(hw8.listOfRunLengths(sequence), [64])  #Test listOfRunLengths
        self.assertEqual(hw8.findRunBits(sequence), 7)          #Test findRunBits
        compress = hw8.compressA(sequence)
        self.assertEqual(compress, '1111000000')                #Test compressA
        uncompress = hw8.uncompressA(compress)
        self.assertEqual(uncompress, sequence)                  #Test uncompressA

    def test02(self):
        sequence = '01' * 32
        self.assertEqual(hw8.listOfRunLengths(sequence), [1]*64)
        self.assertEqual(hw8.findRunBits(sequence), 1)
        compress = hw8.compressA(sequence)
        self.assertEqual(compress, '0011111111111111111111111111111111111111111111111111111111111111111')
        uncompress = hw8.uncompressA(compress)
        self.assertEqual(uncompress, sequence)

    def test03(self):
        sequence = '10' * 32
        self.assertEqual(hw8.listOfRunLengths(sequence), [1]*64)
        self.assertEqual(hw8.findRunBits(sequence), 1)
        compress = hw8.compressA(sequence)
        self.assertEqual(compress, '00101111111111111111111111111111111111111111111111111111111111111111')
        uncompress = hw8.uncompressA(compress)
        self.assertEqual(uncompress, sequence)

    def test04(self):
        sequence = '0' * 31 + '1' * 31 + '00'
        self.assertEqual(hw8.listOfRunLengths(sequence), [31, 31, 2])
        self.assertEqual(hw8.findRunBits(sequence), 6)
        compress = hw8.compressA(sequence)
        self.assertEqual(compress, '110011111011111000010')
        uncompress = hw8.uncompressA(compress)
        self.assertEqual(uncompress, sequence)

    def test05(self):
        sequence = '0' * 32 + '1' * 32
        self.assertEqual(hw8.listOfRunLengths(sequence), [32, 32])
        self.assertEqual(hw8.findRunBits(sequence), 6)
        compress = hw8.compressA(sequence)
        self.assertEqual(compress, '110100000100000')
        uncompress = hw8.uncompressA(compress)
        self.assertEqual(uncompress, sequence)

    def test06(self):
        sequence = '1' * 31 + '0' * 31 + '1' * 2
        self.assertEqual(hw8.listOfRunLengths(sequence), [31, 31, 2])
        self.assertEqual(hw8.findRunBits(sequence), 6)
        compress = hw8.compressA(sequence)
        self.assertEqual(compress, '110000000011111011111000010')
        uncompress = hw8.uncompressA(compress)
        self.assertEqual(uncompress, sequence)

if __name__ == "__main__":
    unittest.main()
