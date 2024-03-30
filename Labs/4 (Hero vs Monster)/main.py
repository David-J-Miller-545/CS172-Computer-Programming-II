# Name: David Miller | djm545

 
from characters import Monster, Hero

import random

# This function has two Characters fight
# it returns the winner or None on a tie
def monster_battle(h1, m1):
   
    print("Starting Battle Between")
    print(m1.getName() + ": " + m1.getDescription())
    print(h1.getName() + ": " + h1.getDescription())
    
    
    #Whose turn is it?
    attacker = None
    defender = None

    ######TODO######    
    attacker = h1 if (random.random() > 0.5) else m1
    defender = h1 if (attacker == m1) else m1
        
    print(attacker.getName() + " goes first.")
    
    #Loop until someone is unconsious (health < 1) or choose to stop
    stop = False
    while( m1.getHealth() > 0 and h1.getHealth() > 0 and not stop ):
        
        #It will be nice for output to record the damage done
        before_health = defender.getHealth()            

        #Check if the attacker is a monster
        if(isinstance(attacker, Monster)):
            #check if defender is defending, if so print out info about the defense
            if(defender.isDefending()):
                print("Our hero is defending with", defender.getDefenseName(), "!")
            print(attacker.react())
            attacker.attack(defender)
            print_results(attacker, defender, attacker.getWeaponName(), (before_health - defender.getHealth()))
            

        else:
            # Ask the user for the next action: attack, defend, or stop.
            action = input('Pick one of these (a)ttack, (d)efend, or sto(p): ')
           
            #Based on the input, either attack, defend, or end loop
            if action == "a":
                #Have the attacker react, attack
                print(attacker.react())
                attacker.attack(defender)
                #call the print_results function with the necessary info.
                print_results(attacker, defender, attacker.getWeaponName(), (before_health - defender.getHealth()))
            elif action == "d":
                attacker.defend()
            elif action == "p":
                stop = True
            else:
                #Incase input validation needed
                pass
            


        #Swap attacker and defender
        temp = attacker
        attacker = defender
        defender = temp
        

    #Return who won.
    if h1.getHealth() > m1.getHealth():
        return h1
    else:
        return m1
    
    
    
    
#This function prints the status updates
def print_results(attacker, defender, attack, hchange):
    res = attacker.getName() + " used " + attack
    res += " on " + defender.getName() + "\n"
    res += "The attack did " + str(hchange) + " damage."
    print(res)
    print(attacker.getName() + " at " + str(attacker.getHealth()))
    print(defender.getName() + " at " + str(defender.getHealth()))

#This inputs all of the Data for a character and returns it as a list
def inputData(uniqueAttribute, hero = False):
    character = "hero" if hero else "monster"
    the = "the" if hero else ""
    # stats = [str name, str description, int maxHealth, str weaponName, float weaponDamage, str uniqueAttribute]
    stats = ["", "", 0, "", float(0), ""]
    stats[0] = input(f"Enter {character}'s name: ")
    stats[1] = input(f"Enter {the} {character}'s description: ")
    stats[2] = int(input(f"Enter a number for {the} {character}'s health: "))
    stats[3] = input(f"Enter {character}'s weapon name: ")
    stats[4] = float(input(f"Enter {character}'s weapon damage (as a number): "))
    stats[5] = input(f"Enter {the} {character}'s {uniqueAttribute}: ")
    return stats
    
#----------------------------------------------------
if __name__=="__main__":
    #Every battle should be different, so we need to
    #start the random number generator somewhere "random".
    #With no input Python will set the seed
    random.seed(0)
     
    #Get Monster's name, description, maxHealth, weaponName, weaponDamage, and motivation from the user here.
    #Instantiate a Monster using that info. Note that weaponDamage should be a floating point number.
    monsterStats = inputData("motivation")
    
    myMonster = Monster(monsterStats[0], monsterStats[1], monsterStats[2], monsterStats[3], monsterStats[4], monsterStats[5])
      
    #Get the Hero's name,description, maxHealth, weaponName, weaponDamage, defenseName from the user here.
    #Instantiate a Hero using that info. Note that weaponDamage should be a floating point number.
    heroStats = inputData("defense name", True)
     
    myHero = Hero(heroStats[0], heroStats[1], heroStats[2], heroStats[3], heroStats[4], heroStats[5])  #this should be an instance of your Hero class
    
    winner = monster_battle(myHero, myMonster)
    print(f"\nBattle is over. let's see who has won...\n{winner.getName()} is victorious!")
