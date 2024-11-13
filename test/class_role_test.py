import unittest
from character import Character
from class_role import FighterClass


class TestFighterClass(unittest.TestCase):
    def setUp(self):
        self.character = Character(name="Astor", prof_bonus=0)
        self.fighter = FighterClass(self.character, hp=20, level=0)
    
    def test_level_up_initial_level(self):
        self.fighter.level_up(proficiencies="Athletics", feats="Archer")
        
        self.assertEqual(self.character.prof_bonus, 2)
        self.assertListEqual(self.character.proficiencies, ["Athletics", "Intimidation"])
        self.assertListEqual(self.fighter.feats, ["Fighting style - Archer", "Retake Breath"])


if __name__ == "__main__":
    unittest.main()
