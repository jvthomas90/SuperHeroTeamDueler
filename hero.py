import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0
        self.alive_status = True

    def fight(self, opponent):
        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("draw")

        else:
            while self.is_alive() and opponent.is_alive():
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())

                if not self.is_alive():
                    print(f" Winner is {opponent.name}")
                    self.add_death(1)
                    opponent.add_kill(1)

                    break

                elif not opponent.is_alive():
                    self.add_kill(1)
                    opponent.add_death(1)
                    print(f" Winner is {self.name}")
                    break

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''

        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0

        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        amount = damage - self.defend()
        self.current_health -= amount

        return self.current_health

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman", 700)
    hero2 = Hero("Dumbledore", 800)

    hero1.fight(hero2)

    hero = Hero("Grace Hopper", 200)
    ability = Ability("Great Debugging", 50)

    hero.add_ability(ability)
    print(hero.abilities)

    ability2 = Ability("left hook", 25)
    hero.add_ability(ability2)
    print(hero.abilities)

    another_ability = Ability("Smarty Pants", 90)
    hero.add_ability(another_ability)
    print(hero.attack())

    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)

    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())

    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
