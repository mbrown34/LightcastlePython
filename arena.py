#!/usr/bin/env python
'''
Created on Oct 1, 2012

@author: josh
'''
import player
import random
import menus
import dice

global level_threshhold
level_threshhold=100
def fight():
   # from enemylist import enemylist
# PICKS AN ENEMY FROM ENEMYLIST FILE
   # opponent=random.choice(enemylist)
  #  opponent.hpmax=opponent.hpmax
  #  enemy_hp=opponent.hpmax
  #  enemy_defend=opponent.defend()
    playerone_hp=player.playerone.hpmax
    your_defend=player.playerone.defend()
    print "You are fighting "+opponent.Name, "\n\tOpponent's max HP:", opponent.hpmax, "\n\tYour HP:", player.playerone.hpmax

    while enemy_hp or playerone_hp >=0:
        enemy_attack=opponent.attack()
        your_attack=player.playerone.attack()
        print
        player_initiative_roll=dice.Die()
        opponent_initiative_roll=dice.Die()
        player_initiative_roll.roll(1, 20)
        player_initiative=player_initiative_roll.total
        opponent_initiative_roll.roll(1,20)
        opponent_initiative=opponent_initiative_roll.total
        
        if player_initiative > opponent_initiative:
            print "Player goes first."
            enemy_hp = playerone_attack_check(your_attack, enemy_defend, enemy_hp, playerone_hp)
            if enemy_hp<=0:
                player.playerone.xp+=opponent.xp_value
                player.playerone.gold+=opponent.gold
                player.playerone.renown+=opponent.renown_value
                check_for_levelup()
                print player.playerone.xp, "\nyou defeated the enemy, returning to main menu"
                break

            playerone_hp = enemy_attack_check(enemy_attack, your_defend, playerone_hp, enemy_hp)
            if playerone_hp<=0:
                print "You were defeated. Returning to main menu"
                #menus.main()
                break
            print "Your hp: ", playerone_hp, "Enemy's hp: ", enemy_hp
        
        elif opponent_initiative>player_initiative:
            print "Opponent goes first."
            playerone_hp = enemy_attack_check(enemy_attack, your_defend, playerone_hp, enemy_hp)
            if playerone_hp<=0:
                print"You were defeated. Returning to main menu"
                #menus.main()
            enemy_hp = playerone_attack_check(your_attack, enemy_defend, enemy_hp, playerone_hp)
            if enemy_hp<=0:
                player.playerone.xp+=opponent.xp_value
                player.playerone.gold+=opponent.gold
                player.playerone.renown+=opponent.renown_value
                check_for_levelup()
                print player.playerone.xp, "\nyou defeated the enemy, returning to main menu"
                #menus.main()
                break
            print "Your hp: ", playerone_hp, "Enemy's hp: ", enemy_hp
        print "END OF TURN\n--------------------------"
	
    #menus.main()

def enemy_attack_check(enemy_attack, your_defend, playerone_hp, enemy_hp):
    if enemy_attack>your_defend:
        print "opponent lands attack"
        enemy_attack=enemy_attack-your_defend
        playeroneHp=playerone_hp-enemy_attack
        print playeroneHp
	return playeroneHp

def playerone_attack_check(your_attack, enemy_defend, enemy_hp, playerone_hp):
    if your_attack>enemy_defend:
        print "player lands attack"
        your_attack=your_attack-enemy_defend
        enemyHp=enemy_hp-your_attack
        print enemyHp
	return enemyHp

def check_for_levelup():
    print "about to check for level up"
    global level_threshhold
    if player.playerone.xp>=level_threshhold:
        print "Checking for level up"
        player.playerone.level+=1
        player.playerone.hpmax+=int(player.playerone.hpmax*.15)
        level_threshhold=int(level_threshhold*.2+level_threshhold)
        print "**** You leveled up! ****\n your new level is: ", player.playerone.level, "your new level threshhold", level_threshhold, "your new hp is: ", player.playerone.hpmax
        player.playerone.xp=0
