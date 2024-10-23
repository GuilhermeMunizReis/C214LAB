import unittest
import sys

sys.path.append('src')

from utils import *

class TestUtils(unittest.TestCase):
    def testDiceInstance(self):
        d = Dice(6)

        self.assertEqual(d.sides, 6)

    def testDiceInstanceError(self):
        d = Dice(8)
        
        self.failureException()
    
if __name__ == '__main__':  
    unittest.main()