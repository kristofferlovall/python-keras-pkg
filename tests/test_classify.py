import unittest

import os

import env

from imrpyml2019 import train, classify

class TestClasify(unittest.TestCase):
    
    def setUp(self):
        # Run training
        self.score = train()
        self.localpath = os.path.dirname(os.path.abspath(__file__ + "/../"))
    
    def test_classify1(self):
        # Test classification #1
        self.assertEqual(classify(self.localpath + "/samples/trousers.jpg"), 1)
    
    def test_classify2(self):
        # Test classification #2
        self.assertEqual(classify(self.localpath + "/samples/ankleboots.jpg"), 9)

if __name__ == '__main__':
    unittest.main()
