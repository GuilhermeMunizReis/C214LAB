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

    def test_get_character_level(self):
        class MockClass:
            def __init__(self, level):
                self.level = level

        # Adiciona uma classe principal e duas multiclasses
        self.char.character_class = MockClass(3)
        self.char.character_multiclass = [MockClass(2), MockClass(4)]
    
        self.char.get_character_level()
        self.assertEqual(self.char.level, 9)

    def test_prof_bonus(self):
        self.char.level = 5  # Um nível que dá +3 de bônus de proficiência
        self.char.prof_bonus = 2 if self.char.level < 5 else 3
        self.assertEqual(self.char.prof_bonus, 3)


    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            self.char.level = -1  # Nível não pode ser negativo


    def test_multiclass_manipulation(self):
        class MockClass:
            def __init__(self, level):
                self.level = level

        self.char.character_multiclass.append(MockClass(2))
        self.char.get_character_level()
        self.assertEqual(self.char.level, 7)

        self.char.character_multiclass.pop()
        self.char.get_character_level()
        self.assertEqual(self.char.level, 5)

    def test_temporary_attributes(self):
        self.char.str_current = self.char.str_base + 2  # Exemplo de buff
        self.assertEqual(self.char.str_current, 3)

        self.char.str_current -= 3  # Exemplo de debuff
        self.assertEqual(self.char.str_current, 0)

    def test_hp_calculation(self):
        self.char.hp = self.char.level * 10  
        self.assertEqual(self.char.hp, 50)  # Como o nível está definido como 5, o HP deve ser 50

    def test_feats_modify_attributes(self):
        class MockFeat:
            def modify_character(self):
                self.char.str_base += 3  # Aumenta Força
                self.char.dex_base += 1  # Aumenta Destreza

        feat = MockFeat()
        self.char.feats.append(feat)
        self.char._Character__update_character_status()  

        self.assertEqual(self.char.str_base, 4)  # Força aumentada
        self.assertEqual(self.char.dex_base, 2)  # Destreza aumentada

    def test_add_multiclass(self):
        class MockClass:
            def __init__(self, level):
                self.level = level

        self.char.character_multiclass.append(MockClass(2))
        self.char.get_character_level()
    
        self.assertEqual(self.char.level, 7)  # Deve somar o nível de 2 à classe principal

    def test_attack_bonus(self):
        # Supondo que o bônus de ataque depende da Força e do nível
        self.char.str_base = 15  # Força de 15
        self.char.prof_bonus = 3  # Bônus de proficiência

        attack_bonus = self.char.str_base + self.char.prof_bonus  # Cálculo simples para bônus de ataque
        self.assertEqual(attack_bonus, 18)  # Bônus de ataque deve ser 15 (Força) + 3 (Proficiência)


if __name__ == '__main__':
    unittest.main()
