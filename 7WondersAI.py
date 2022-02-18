# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 20:35:16 2022

@author: benjm
"""

import random

turn = 1
playableCard = 0

class Player:
    def __init__(self, wonder, gold, buildings, resources, mpower, vp, hand):
        self.wonder = wonder
        self.gold = gold
        self.buildings = buildings
        self.resources = resources
        self.mpower = mpower
        self.vp = vp
        self.hand = hand
        
class Wonder:
    def __init__(self, resource, s1cost, s1resource, s1effect, s2cost, s2resource, s2effect, s3cost, s3resource, s3effect):
        self.resource = resource
        self.s1cost = s1cost
        self.s1resource = s1resource
        self.s1effect = s1effect
        self.s2cost = s2cost
        self.s2resource = s2resource
        self.s2effect = s2effect
        self.s3cost = s3cost
        self.s3resource = s3resource
        self.s3effect = s3effect

        
class Card:
    def __init__(self, cost, produce, chain, effect, age):
        self.cost = cost
        self.produce = produce
        self.chain = chain
        self.effect = effect
        self.age = age

    
#Age 1 Cards
clayPool = Card(0, "clay", 0, 0, 1)
lumberYard = Card(0, "wood", 0, 0, 1)
altar = Card(0, "2vp", "temple", 0, 1)
clayPitt = Card("1g", "clay or ore", 0, 0, 1)
timberYard = Card("1g", "stone or wood", 0, 0, 1)
westTradingPost = Card(0, 0, "forum", "1 less g raw res left", 1)
loom = Card(0, "loom", 0, 0, 1)
glassworks = Card(0, "glass", 0, 0, 1)
press = Card(0, "papyrus", 0, 0, 1)
workshop = Card("glass", "cog", "laboratory", 0, 1)
barracks = Card("ore", "1mp", 0, 0, 1)
stockade = Card("wood", "1mp", 0, 0, 1)
guardTower = Card("clay", "1mp", 0, 0, 1)
apothecary = Card("loom", "compass", "stables or dispensary", 0, 1)
scriptorium = Card("papyrus", "tablet", "courthouse or library", 0, 1)
eastTradingPost = Card(0, 0, "forum", "1 less g raw res right", 0, 1)
marketplace = Card(0, 0, "caravansery", "1 less g man res both", 1)
baths = Card("stone", "3vp", "aqueduct", 0, 1)
theater = Card(0, "2vp", "statue", 0, 1)
stonePit = Card(0, "stone", 0, 0, 1)

cards1 = [clayPool, lumberYard, altar, clayPitt, timberYard, westTradingPost, loom, glassworks, barracks, stockade, guardTower, apothecary, scriptorium, eastTradingPost, marketplace, baths, theater, stonePit]

#wonders
alexandriaA = Wonder("glass", ["stone", "stone"], "3vp", 0, ["ore", "ore"], "raw", 0, ["glass", "glass"], "7vp", 0)
halikarnassosA = Wonder("loom", ["clay", "clay"], "3vp", 0, ["ore", "ore", "ore"], 0, "pick discarded", ["loom", "loom"], "7vp", 0)
gizahA = Wonder("stone", ["stone", "stone"], "3vp", 0, ["wood", "wood", "wood"], "5vp", 0, ["stone", "stone", "stone", "stone"], "7vp", 0)
olympiaA = Wonder("wood", ["wood" "wood"], "3vp", 0, ["stone", "stone"], 0, "free card", ["ore", "ore"], "7vp", 0)
ephesosA = Wonder("papyrus", ["stone", "stone"], "3vp", 0, ["wood", "wood"], "9g", 0, ["papyrus", "papyrus"], "7vp", 0)
babylonA = Wonder("clay", ["clay", "clay"], "3vp", 0, ["wood", "wood", "wood"], "science", 0, ["clay", "clay", "clay", "clay"], "7vp", 0)
rhodosA = Wonder("ore", ["wood", "wood"], "3vp", 0, ["clay", "clay", "clay"], "3mp", 0, ["ore", "ore", "ore", "ore"], "7vp", 0)

wonders = [alexandriaA, halikarnassosA, gizahA, olympiaA, ephesosA, babylonA, rhodosA]

class GameState:
    def __init__(self):
        pass
    def startState():
        random.shuffle(wonders)
        random.shuffle(cards1)        
        
def playGame():
    GameState.startState()
    if turn == 1:
        player1 = Player(wonders[0], 3, [], [], 0, 0, [])
        player2 = Player(wonders[1], 3, [], [], 0, 0, [])
        player3 = Player(wonders[2], 3, [], [], 0, 0, [])
        players = [player1, player2, player3]
        
        for i in players:
            players[i].resources.append(players[i].wonder.resource) #give player their wonders starting resource
            
        for i in players:
            for j in range(7):
                players[i].hand.append(cards1[i*7 + j]) #give players thier starting hands
    
    while turn <= 7:
        for i in players:
            for j in players[i].hand:
                if players[i].hand[j].cost == 0:
                    playableCard.append(j)
                elif players[i].hand[j].cost in players[i].resources:
                    playableCard.append(j)
                elif players[i].hand[j].cost in players[]
                    
                    
        
        
    








        