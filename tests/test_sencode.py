import unittest
import sencode

import numpy as np

class TestEncode(unittest.TestCase):
    def test_blosum62(self):
        self.assertEqual(sencode.blosum62.loc['H', 'G'], -2)
        self.assertEqual(sencode.blosum62.loc['P', 'C'], -3)
    def test_encode_blosum62(self):
        seq = 'ARNWYV'
        seq_b62 = sencode.encode_blosum62(seq)
        self.assertEqual(seq_b62[0][1], -1)
        self.assertEqual(seq_b62[5][19], 4)
    def test_encode_onehot(self):
        seq = 'ARNWYV'
        seq_onehot = sencode.encode_onehot(seq)
        self.assertListEqual(list(seq_onehot[0]),
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0])
