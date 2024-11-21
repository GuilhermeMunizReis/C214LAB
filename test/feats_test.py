import unittest
from character import Character
from feats import Defense, Tough, Sharpshooter, Alert, MagicInitiate

class TestFeats(unittest.TestCase):
    
    def setUp(self):
        # Criando o personagem para realizar os testes:
        self.character = Character(name="Claudia", race="Human", level=5)
        
    def test_defense_feat(self):
        defense_feat = Defense()
        defense_feat.modify_character(self.character)

        # Verifica se o AC foi aumentado em 1
        self.assertEqual(self.character.ac, 1)  # Supondo que o AC inicial seja 0, e o aumento seja de 1
    
    def test_tough_feat(self):
        tough_feat = Tough()
        tough_feat.modify_character(self.character)
        
        # Verifica se o HP foi aumentado corretamente
        self.assertEqual(self.character.hp, 10)  # O HP deve ser aumentado em 2 * level (2 * 5 = 10)
    
    def test_sharpshooter_feat(self):
        sharpshooter_feat = Sharpshooter()
        sharpshooter_feat.modify_character(self.character)
        
        self.assertIn("Sharpshooter", self.character.proficiencies)
        self.assertEqual(self.character.attack_damage_modifier, 2)  # O dano de ataque à distância foi dobrado
        self.assertTrue(self.character.can_ignore_cover)  # O personagem deve ser capaz de ignorar cobertura
    
    def test_alert_feat(self):
        alert_feat = Alert()
        alert_feat.modify_character(self.character)
        
        self.assertIn("Alert", self.character.proficiencies)
        self.assertEqual(self.character.prof_bonus, 2)  # O bônus de proficiência deve ser aumentado
    
    def test_magic_initiate_feat(self):
        magic_feat = MagicInitiate(caster_class="Wizard")
        magic_feat.modify_character(self.character)
        
        # Verifica se o personagem recebeu os cantrips e feitiços esperados
        self.assertIn("Magic Initiate: Wizard", self.character.feats)
        self.assertIn("Firebolt", self.character.feats[-1])  # O cantrip Firebolt deve estar na lista
        self.assertIn("Shield", self.character.feats[-1])  # O feitiço Shield deve estar na lista
    
    # Teste para a feat Magic Initiate com requisitos não atendidos
    def test_magic_initiate_feat_invalid(self):

        character_invalid = Character(name="Lucas", race="Human", level=5, int_value=10)  # Não tem Inteligência suficiente
        magic_feat_invalid = MagicInitiate(caster_class="Wizard")
        magic_feat_invalid.modify_character(character_invalid)
        
        # Verifica se o personagem não recebeu os feitiços
        self.assertNotIn("Magic Initiate", character_invalid.feats)
        
    # Teste para aplicar múltiplas feats no mesmo personagem
    def test_multiple_feats_applied(self):
        character = Character(name="Adriano", race="Human", level=5, int_value=14)
        
        # Aplica a feat Defense e Tough
        defense_feat = Defense()
        tough_feat = Tough()
        defense_feat.modify_character(character)
        tough_feat.modify_character(character)
        
        self.assertEqual(character.ac, 1)  # Defense aumentou o AC em 1
        self.assertEqual(character.hp, 10)  # Tough aumentou o HP em 2 * level (2 * 5 = 10)

    # Testa se a feat Sharpshooter permite ignorar cobertura
    def test_sharpshooter_with_cover(self):
        character = Character(name="Robertinha", race="Elf", level=5)
        
        sharpshooter_feat = Sharpshooter()
        sharpshooter_feat.modify_character(character)
        
        self.assertTrue(character.can_ignore_cover)  # O personagem deve ignorar cobertura ao atacar
        
        # Simula um ataque à distância com cobertura (deve ignorar a cobertura)
        cover_present = True
        attack_result = self.simulate_ranged_attack(character, cover_present)
        self.assertEqual(attack_result, "Attack successful, cover ignored!")  


    # Testa se a feat Sharpshooter exige proficiência com armas à distância
    def test_sharpshooter_requires_proficiency(self):
        character_without_proficiency = Character(name="Guilherme", race="Human", level=5, proficiencies=[])
        
        sharpshooter_feat = Sharpshooter()
        sharpshooter_feat.modify_character(character_without_proficiency)
        
        self.assertNotIn("Sharpshooter", character_without_proficiency.proficiencies)  # O personagem não tem a feat devido à falta de proficiência

    # Testa se a feat Tough aumenta corretamente os pontos de vida ao subir de nível
    def test_tough_hp_increase_on_level_up(self):
        
        character = Character(name="Robertinho", race="Human", level=4, hp=10)  
        
        tough_feat = Tough()
        tough_feat.modify_character(character)
        
        self.assertEqual(character.hp, 18)  # O HP deve ser aumentado em 2 * level (2 * 4 = 8), então 10 + 8 = 18
        
        character.level = 5
        tough_feat.modify_character(character)  # Aplica novamente a feat com o novo nível
        
        self.assertEqual(character.hp, 28)  # O HP deve ser aumentado em 2 * level (2 * 5 = 10), então 18 + 10 = 28

    
if __name__ == '__main__':
    unittest.main()
