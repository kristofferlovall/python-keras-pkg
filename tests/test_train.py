import unittest

import env

from imrpyml2019 import train, classify

class TestTrain(unittest.TestCase):
    
    def setUp(self):
        # Run training
        self.score = train()
    
    def test_train_accuracy(self):
        # Determine whether the model accuracy is too low
        self.assertTrue(self.score > 0.8)
    
if __name__ == '__main__':
    unittest.main()
