import unittest
import sys

sys.path.append('src')

from character import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.char = Character("Astor", "Human",  5)

    def testCharacterInstance(self):
        self.assertEqual(self.char.name, "Astor")
        self.assertEqual(self.char.race, "Human")
        self.assertEqual(self.char.character_multiclass, [])
        self.assertEqual(self.char.level, 5)

if __name__ == '__main__':
    unittest.main()
