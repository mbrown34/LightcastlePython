#!/usr/bin/env python
'''
Created on Oct 3, 2012

@author: josh
'''
import player
import store
import fight
import generator


def main():
    print """\n\n\n\n
    You have the following options:
    \t1: Create your character.
    \t2: Enter the store.
    \t3: Enter the arena to fight.
    \t4: Display player information.
    \t5: Change weapon and armor loadout.
    \t6: Quit
                             Enter a number and press enter."""
    player_choice=input("\n>>")
    if player_choice==1:
	character = generator.Character()
	player = character.genChar()	
    elif player_choice==2:
        store.main()
    elif player_choice==3:
        arena.fight()
    elif player_choice==4:
        info()
    elif player_choice==5:
        change_equipment()
    elif player_choice==6:
        endgame = True
	return endgame
    else:
        main()
 
def change_equipment():
    print """\n\n\n\n\nThe following items are equippable by you:"""
    print
    i=1
    for x in player.playerone.equipment:
        print "\t",i, x
        i+=1
    print "\nWhat would you like to equip?"
    equip_this=input(">>")
    player.playerone.equip(player.playerone.equipment[equip_this-1])
    #main()

def info():
    print "This is your character's information:\n\tName: ", player.playerone.Name," \n\tlevel: ", player.playerone.level, "\n\thpmax: ", player.playerone.hpmax, "\n\tbase attack: ", player.playerone.base_attack, "\n\tbase defense vale: ", player.playerone.base_defense, "\n\tgold: ", player.playerone.gold
    player.playerone.display_equipped()
#    for item in player.playerone.equipped_items:
#        print "\t", item, "attack value: ", item.attack_value, "defense value: ", item.defense_value
    player.playerone.display_inventory()
    advance_screen=raw_input("PRESS ENTER TO ADVANCE TO MAIN MENU")
    #main()


