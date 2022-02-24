# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 20:35:16 2022

@author: benjm
"""

import random
import copy

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
    def __init__(self, cost, produce, chain, effect, goldCost):
        self.cost = cost
        self.produce = produce
        self.chain = chain
        self.effect = effect
        self.goldCost = goldCost

    
#Age 1 Cards
clayPool = Card(0, "clay", 0, 0, 0)
lumberYard = Card(0, "wood", 0, 0, 0)
altar = Card(0, "2vp", "temple", 0, 0)
clayPit = Card("gold", "clay or ore", 0, 0, 1)
timberYard = Card("gold", "stone or wood", 0, 0, 1)
westTradingPost = Card(0, 0, "forum", "1 less g raw res left", 0)
loom = Card(0, "loom", 0, 0, 0)
glassworks = Card(0, "glass", 0, 0, 0)
press = Card(0, "papyrus", 0, 0, 0)
workshop = Card("glass", "cog", "laboratory", 0, 0)
barracks = Card("ore", "1mp", 0, 0, 0)
stockade = Card("wood", "1mp", 0, 0, 0)
guardTower = Card("clay", "1mp", 0, 0, 0)
apothecary = Card("loom", "compass", "stables or dispensary", 0, 0)
scriptorium = Card("papyrus", "tablet", "courthouse or library", 0, 0)
eastTradingPost = Card(0, 0, "forum", "1 less g raw res right", 0)
marketplace = Card(0, 0, "caravansery", "1 less g man res both", 0)
baths = Card("stone", "3vp", "aqueduct", 0, 0)
theater = Card(0, "2vp", "statue", 0, 0)
stonePit = Card(0, "stone", 0, 0, 0)
oreVein = Card(0, "ore", 0, 0, 0)

cards1 = [oreVein, clayPool, lumberYard, altar, clayPit, timberYard, westTradingPost, loom, glassworks, press, workshop, barracks, stockade, guardTower, apothecary, scriptorium, eastTradingPost, marketplace, baths, theater, stonePit]

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
        
        for i in range(3):
            players[i].resources.append(players[i].wonder.resource) #give player their wonders starting resource
            
        for i in range(3):
            for j in range(7):
                players[i].hand.append(cards1[i*7 + j]) #give players thier starting hands
        
    while turn < 7:
        if turn != 1:
            handCopy = copy(players[0].hand)
            players[0].hand = players[1].hand
            players[1].hand = players[2].hand
            players[2].hand = handCopy
        for i in range(3):
            playableCards = []
            for j in range(len(players[i].hand)):
                if players[i].hand[j].cost == 0: #If card is free
                    playableCards.append(players[i].hand[j])
                elif players[i].hand[j].cost == "gold" and players[i].gold >= players[i].hand[j].goldCost: #If card costs gold and player can afford
                    playableCards.append(players[i].hand[j])
                else: #Goes to check needs and baskets
                    needs = players[i].hand[j].cost
                    resources = players[i].resources
                    resolvedNeeds = resolveNeeds(needs, resources)
                    
                    if resolvedNeeds == []:
                        playableCards.append(players[i].hand[j])
                    else:
                        resolvedNeedsNum = len(resolvedNeeds[0])
                        for k in range(3):
                            if k == i:
                                continue
                            else:
                                neighbourResolvedNeeds = resolveNeeds(resolvedNeeds, players[k].resources)
                                if neighbourResolvedNeeds == []:
                                    playableCards.append(players[i].hand[j])
                                else:
                                    for l in range(3):
                                        if l == k or l == i:
                                            continue
                                        else:
                                            neighbour2ResolvedNeeds = resolveNeeds(neighbourResolvedNeeds, players[l].resources)
                                    if neighbour2ResolvedNeeds == []:
                                        playableCards.append(players[i].hand[j])
    print(playableCards)
                                
        
#Given a list of needs and a list of resource "baskets" this function returns
#the minimal list of resources that cannot be satisfied.
    
def resolveNeeds(needs, resources):
    finalStates = []
    needsStates = [(needs, resources)]
    
    while needsStates != []:
        firstState = needsStates.pop(0)
        if firstState in finalStates:
            continue
        resolutions = resolveNeed(*firstState)
        if resolutions == []:
            finalStates = updateFinalStates(firstState, finalStates)
        else:
            needsStates = needsStates + resolutions
    if finalStates == []:
        return []
    else:
        return [s[0] for s in finalStates]

#Given list of need and list of resource baskets, returns each way ONE given need
#is resolved by ONE given basket. Therefore returns a list of states with one less
#need and one less basket.
        
def resolveNeed(needs, resources):
    resolutions = []
    
    for need in needs:
        for basket in resources:
            if need in basket:
                otherNeeds = copy(needs)
                otherNeeds.remove(need)
                otherResources = copy(resources)
                otherResources.remove(basket)
                resolutions.append((otherNeeds, otherResources))
    return resolutions

#Checks new final state against existing ones, if it has more un-met needs than an
#existing one it will not be added. If an existing final state has more un-met needs
#then it will be removed.

def updateFinalStates(state, finalStates):
    unbeatenFinalStates = []
    
    for fs in finalStates:
        comp = compareBags(state[0], fs[0])
        if comp == "superbag" or comp == "equal":
            return finalStates
        if comp != "subbag":
            unbeatenFinalStates.append(fs)
        unbeatenFinalStates.append(state)
        return unbeatenFinalStates

#Compares 2 bags.

def compareBags(bag1, bag2):
    cbag2 = copy(bag2)
    only1 = []
    
    for item in bag1:
        if item in cbag2:
            cbag2.remove(item)
        else:
            only1.append(item)
    if only1 == [] and cbag2 == []:
        return "equal"
    if only1 == []:
        return "subbag"
    if cbag2 == []:
        return "superbag"
    return "incomparable"

playGame()
        
        
    








        