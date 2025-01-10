"""import random
import os
import time
from playsound import playsound

def play_sound(sound_name):
    sound_files = {
        "intro_theme": "sounds/intro_theme.mp3",
        "door_creak": "sounds/door_creak.mp3",
        "door_open": "sounds/door_open.mp3",
        "monster_roar": "sounds/monster_roar.mp3",
        "sword_swing": "sounds/sword_swing.mp3",
        "healing_spell": "sounds/healing_spell.mp3",
        "monster_attack": "sounds/monster_attack.mp3",
        "victory": "sounds/victory.mp3",
        "game_over": "sounds/game_over.mp3",
        "treasure_open": "sounds/treasure_open.mp3",
        "cheering_crowd": "sounds/cheering_crowd.mp3",
        "trap": "sounds/trap.mp3"
    }
    try:
        if sound_name in sound_files:
            playsound(sound_files[sound_name])
        else:
            print(f"[Sound: {sound_name} not found.]")
    except Exception as e:
        print(f"[Error playing sound '{sound_name}': {e}]")

def display_intro():
    play_sound("intro_theme")
    print("Welcome to the Pirate's Adventure!")
    print("You are an pirate seeking treasure in a dark and dangerous sea")
    print("Your decisions will lead you to your result")
    play_sound("door_creak")

def choose_path():
    print("\nTwo doors appear before you:")
    print("1. A door glowing faintly with blue light.")
    print("2. one that is covered in vines")
    choice = input("Which way yer choice? (1/2): ")
    while choice not in ['1', '2']:
        choice = input("are oyu blind there is no option rather then those two doors (1/2): ")
    play_sound("door_open")
    return int(choice)

def battle_monster():
    play_sound("monster_roar")
    print("\nA wild monster appeared to snatch your doubloons")
    player_health = 20
    monster_health = 15

    while player_health > 0 and monster_health > 0:
        print(f"Your Health: {player_health}, Monster Health: {monster_health}")
        action = input("Do you attack or freak out and heal? (attack/heal): ")
        if action.lower() == "attack":
            damage = random.randint(5, 10)
            monster_health -= damage
            print(f"You  gave {damage} damage to the monster!")
            play_sound("sword_swing")
        elif action.lower() == "heal":
            heal = random.randint(3, 8)
            player_health += heal
            print(f"You healed yourself for {heal} health!")
            play_sound("healing_spell")
        else:
            print("you went wrong here")

        if monster_health > 0:
            damage = random.randint(4, 8)
            player_health -= damage
            print(f"The monster gave {damage} damage to you")
            play_sound("monster_attack")

    if player_health > 0:
        print("\nFirst step towards the main battle")
        play_sound("victory")
        return True
    else:
        print("\noh! no pirate he got you.. Game over!")
        play_sound("game_over")
        return False

def find_treasure():
    play_sound("treasure_open")
    print("\nThere goes some shiny doubloons for fw13!")
    doubloons = random.randint(1320, 1370)
    print(f"You collect {doubloons} doubloons and updates are coming soon")
    play_sound("cheering_crowd")

def play_game():
    display_intro()
    path = choose_path()

    if path == 1:
        survived = battle_monster()
        if survived:
            find_treasure()
    else:
        print("\nSome times you need to choose you path wisely this is life not a game Life over!")
        play_sound("trap")

play_game()"""
