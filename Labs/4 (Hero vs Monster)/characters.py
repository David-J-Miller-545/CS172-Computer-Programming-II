# Name: David Miller | djm545


# This class defines a generic Character
# It includes attributes and many implemented methods, in addition to an abstract
# methods __str__ and react
from abc import ABC, abstractmethod

### DO NOT CHANGE ANYTHING BELOW IN THIS Character CLASS ####
class Character(ABC):
    def __init__(self, name, description, maxHealth, weaponName, weaponDamage):
        self.__name = name
        self.__health = maxHealth
        self.__description = description
        self.__weaponName = weaponName
        self.__weaponDamage = weaponDamage

    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def react(self):
        pass
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description
    
    def getWeaponName(self):
        return self.__weaponName
    
    def getWeaponDamage(self):
        return self.__weaponDamage
    
    def attack(self, enemy):
        enemy.takeDamage(self.__weaponDamage)
    
    def takeDamage(self, amount):
        self.__health -= amount
    
    def getHealth(self):
        return self.__health
    
    
class Monster(Character):
    def __init__(self, name, description, maxHealth , weaponName, weaponDamage, motivation):
        super().__init__(name, description, maxHealth , weaponName, weaponDamage)
        self.__motivation = motivation
        
    def __str__(self):
        string =  f"{self.getName()} is a {self.getDescription()}\n"
        string += f"Weapon: {self.getWeaponName()}\n"
        string += f"Current Health: {self.getHealth()}\n"
        string += f"Motivation: {self.__motivation}"
        return string
    
    def react(self):
        return f"{self.getName()} laughs maniacally."
    
    def getMotivation(self):
        return self.__motivation


class Hero(Character):
    def __init__(self, name, description, maxHealth, weaponName, weaponDamage, defenseName):
        super().__init__(name, description, maxHealth , weaponName, weaponDamage)
        self.__defenseName = defenseName
        self.__defenseStatus = False
        pass
        
    def __str__(self):
        string =  f"Our hero {self.getName()} is a {self.getDescription()}\n"
        string += f"Weapon: {self.getWeaponName()}\n"
        string += f"Defense: {self.getDefenseName()}\n"
        string += f"Current Health: {self.getHealth()}\n"
        string += f"Defense Status: {self.isDefending()}"
        return string
        
    def react(self):
        return f"{self.getName()} charges bravely."
        
    def getDefenseName(self):
        return self.__defenseName  
    
    def isDefending(self):
        return self.__defenseStatus
    
    def defend(self):
        self.__defenseStatus = True
        
    def takeDamage(self, amount):
        if self.__defenseStatus:
            amount *= .5
            self.__defenseStatus = False
        super().takeDamage(amount)
