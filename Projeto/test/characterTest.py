# characterTest.py
import unittest
import sys

sys.path.append('src')

from character import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.char = Character("Eldrin", "Ranger", 5)

    def testCharacterInstance(self):
        self.assertEqual(self.char.name, "Eldrin")
        self.assertEqual(self.char.character_class, "Ranger")
        self.assertEqual(self.char.level, 5)

    def testLevelUp(self):
        self.char.level_up()
        self.assertEqual(self.char.level, 6)

if __name__ == '__main__':
    unittest.main()
