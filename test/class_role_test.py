import unittest
from character import Character
from class_role import FighterClass


class TestFighterClass(unittest.TestCase):
    def setUp(self):
        self.character = Character(name="Astor", race="Human", level=0)
        self.fighter = FighterClass(self.character, hp=20, level=1)
    
    """
    def test_level_up_initial_level(self):
        self.fighter.level_up(proficiencies="Athletics", feats="Archer")
        
        self.assertEqual(self.character.prof_bonus, 2)
        self.assertListEqual(self.character.proficiencies, ["Athletics", "Intimidation"])
        self.assertListEqual(self.fighter.feats, ["Fighting style - Archer", "Retake Breath"])
    """
    
    def test_character_class_assignment(self):
        # O personagem deve ter a classe Fighter associada corretamente
        self.assertEqual(self.fighter.character, self.character)
        self.assertIsInstance(self.fighter, FighterClass)

    def test_fighter_class_initial_hp(self):
        # O HP inicial deve ser 20
        self.assertEqual(self.fighter.total_hp, 20)


class TestFighterClassLevelUpWithMultipleFeatsAndProficiencies(unittest.TestCase):
    def setUp(self):
        self.character = Character(name="Astor", race="Human", level=2)
        self.fighter = FighterClass(self.character, hp=30, level=2)

    def test_level_up_with_multiple_feats(self):
        # Antes do level up
        self.assertEqual(self.fighter.level, 2)
        self.assertListEqual(self.character.proficiencies, [])
        self.assertEqual(self.fighter.feats, [])

        # Aplicando level up com várias proficiências e feats
        self.fighter.level_up(proficiencies=["Athletics", "Survival"], feats="Fighting style - Great Weapon Fighting")

        # Verificando as mudanças
        self.assertEqual(self.fighter.level, 3)
        self.assertListEqual(self.character.proficiencies, ["Athletics", "Survival"])
        self.assertIn("Fighting style - Great Weapon Fighting", self.fighter.feats)

    # Level Up
    def test_level_up_increases_level(self):
        
        initial_level = self.fighter.level
        
        self.fighter.level_up(proficiencies=["Athletics", "Survival"], feats="Fighting style - Great Weapon Fighting")
        
        self.assertEqual(self.fighter.level, initial_level + 1)

    def test_no_duplicate_feats(self):
        # Realizando o level up pela primeira vez
        self.fighter.level_up(proficiencies=["Athletics", "Survival"], feats="Fighting style - Great Weapon Fighting")
        
        # Realizando o level up novamente com o mesmo feat
        self.fighter.level_up(proficiencies=["Athletics", "Survival"], feats="Fighting style - Great Weapon Fighting")
        
        # Verificando se o feat não foi duplicado
        self.assertEqual(self.fighter.feats.count("Fighting style - Great Weapon Fighting"), 1)

    def test_level_up_without_feats_or_proficiencies(self):
        # Realizando o level up sem fornecer feats ou proficiências
        self.fighter.level_up(proficiencies=[], feats="")
        
        # As proficiências e feats não devem ser alterados
        self.assertEqual(self.character.proficiencies, [])
        self.assertEqual(self.fighter.feats, [])
    

if __name__ == "__main__":
    unittest.main()
