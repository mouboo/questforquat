#!/usr/bin/env python3
#game.py

from player import Player
import world
from collections import OrderedDict
import os
import art

def play():
    os.system('cls||clear')
    input(art.qfq_banner)
    world.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        os.system('cls||clear')
        print("#" * 30 + " THE QUEST FOR QUAT " + "#" * 30)
        room = world.tile_at(player.x,player.y)
        print(room.intro_text())
        if room.menace_text():
            print(room.menace_text())
        if room.floor_items:
            print(room.floor_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room,player)
        elif not player.is_alive():
            print("Your journey has come to an early end.")

def get_player_command():
    return input('> ')

def get_available_actions(room,player):
    actions = OrderedDict()
    print("Choose an action: ")
    action_adder(actions, 'i', player.print_inventory, "Inventory")
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")
    if room.floor_items:
        action_adder(actions, 'p', player.pick_up_item, "Pick up item")
    action_adder(actions,'u', player.utter, "Utter")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
    else:
        print("--------------")
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go north")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go west")
    if player.hp < 100:
        action_adder(actions, 'h', player.heal, "Heal")
    return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey,name)) 

def choose_action(room,player):
    action = None
    while not action:
        available_actions = get_available_actions(room,player)
        action_input = input("> ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action.")

play()
