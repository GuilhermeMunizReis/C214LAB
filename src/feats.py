# Importação das bibliotecas necessárias
from abc import ABC, abstractmethod
from character import Character


class Feat(ABC):
    def __init__(self):
        self.feat = ""        
        self.description = ""    
        self.requirements = ""    
    
    @abstractmethod
    def modify_character(self, character: Character):
        pass 


class Defense(Feat):
    def __init__(self):
        super().__init__()
        self.feat = "Defense"  
        self.description = "+1 AC when using a armor" 
        self.requirements = "No requirements"  

    def modify_character(self, character: Character):
        character.ac += 1

# Aumenta os pontos de vida máximos do personagem
class Tough(Feat):
    def __init__(self):
        super().__init__()
        self.feat = "Tough"  
        self.description = "Increases maximum hit points by 2 per level"  
        self.requirements = "Requires level 4 or higher"  

    def modify_character(self, character: Character):
        # Aumenta o HP do personagem em 2 vezes o seu nível
        character.hp += 2 * character.level

# Melhora as habilidades com ataques à distância
class Sharpshooter(Feat):
    def __init__(self):
        super().__init__()
        self.feat = "Sharpshooter"  
        self.description = "Ignore cover and increase long-range attack damage."  
        self.requirements = "Requires proficiency with ranged weapons"  # Requisito: proficiência com armas à distância

    def modify_character(self, character: Character):
        character.proficiencies.append("Sharpshooter")

        character.attack_damage_modifier = 2  # Modifica o dano de ataques à distância, dobrando o valor

        # Se o personagem tiver a feat, ele pode ignorar cobertura ao atacar
        character.can_ignore_cover = True

        print(f"{character.name} now has the Sharpshooter feat. Their ranged attacks deal double damage and they ignore cover.")


# Aumenta a iniciativa do personagem e o impede de ser surpreendido
class Alert(Feat):
    def __init__(self):
        super().__init__()
        self.feat = "Alert"  
        self.description = "Increase initiative and prevent being surprised." 
        self.requirements = "No requirements"  

    def modify_character(self, character: Character):
        character.proficiencies.append("Alert")
        character.prof_bonus += 2

# Permite ao personagem lançar feitiços de uma classe mágica
class MagicInitiate(Feat):
    def __init__(self, caster_class: str):
        super().__init__()
        self.feat = "Magic Initiate"  
        self.description = "Gain the ability to cast a few cantrips and 1st-level spells from a chosen magic class."  
        self.requirements = "Requires Intelligence, Wisdom, or Charisma of 13+"  
        self.caster_class = caster_class  # Classe mágica escolhida (ex: Mago, Feiticeiro, Bruxo)
        self.cantrips = []  # Lista de cantrips (magias de baixo nível)
        self.first_level_spells = []  # Lista de feitiços de 1º nível
    
    def modify_character(self, character: Character):
        # Verifica se o personagem tem um atributo necessário para adquirir a feat
        if character.int_value >= 13 or character.wis_value >= 13 or character.cha_value >= 13:
            # Escolha de classe mágica (Mago, Feiticeiro, Bruxo) e feitiços associados
            if self.caster_class == "Wizard":
                self.cantrips = ["Firebolt", "Mage Hand"]
                self.first_level_spells = ["Shield", "Magic Missile"]
            elif self.caster_class == "Sorcerer":
                self.cantrips = ["Ray of Frost", "Prestidigitation"]
                self.first_level_spells = ["Mage Armor", "Burning Hands"]
            elif self.caster_class == "Warlock":
                self.cantrips = ["Eldritch Blast", "Chill Touch"]
                self.first_level_spells = ["Hex", "Armor of Agathys"]
            else:
                # Caso o jogador forneça uma classe mágica inválida
                print(f"{character.name} chose an invalid caster class.")

            # Adiciona os feitiços e cantrips ao personagem
            character.feats.append(f"Magic Initiate: {self.caster_class} - Cantrips: {', '.join(self.cantrips)} | Spells: {', '.join(self.first_level_spells)}")
        else:
            # Caso os requisitos não sejam atendidos
            print(f"{character.name} doesn't meet the requirements for Magic Initiate.")
