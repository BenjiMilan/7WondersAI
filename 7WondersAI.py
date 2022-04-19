# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 20:35:16 2022

@author: Benjamin Milan
"""

import random
from copy import copy


class Player:
    def __init__(self, wonder, gold, buildings, resources, mpower, vp, hand, chains, name, science, effects, ai):
        self.wonder = wonder
        self.gold = gold
        self.buildings = buildings
        self.resources = resources
        self.mpower = mpower
        self.vp = vp
        self.hand = hand
        self.chains = chains
        self.name = name
        self.science = science
        self.effects = effects
        self.ai = ai
        
class Wonder:
    def __init__(self, name, resource, stage1, stage2, stage3):
        self.name = name
        self.resource = resource
        self.stage1 = stage1
        self.stage2 = stage2
        self.stage3 = stage3

        
class Card:
    def __init__(self, cost, produce, chain, effect, goldCost, name, colour, neighbourPay):
        self.cost = cost
        self.produce = produce
        self.chain = chain
        self.effect = effect
        self.goldCost = goldCost
        self.name = name
        self.colour = colour
        self.neighbourPay = neighbourPay
    
class ai:
    def __init__(self, goldValue1, goldValue2, goldValue3, scienceFocus, militaryFocus):
        self.goldValue1 = goldValue1
        self.goldValue2 = goldValue2
        self.goldValue3 = goldValue3
        self.scienceFocus = scienceFocus
        self.militaryFocus = militaryFocus

#Age 1 Cards
clayPool = Card(0, [["clay"]], 0, 0, 0, "Clay Pool", "brown", [])
lumberYard = Card(0, [["wood"]], 0, 0, 0, "Lumber Yard", "brown", [])
altar = Card(0, 2, ["Temple"], 0, 0, "Altar", "blue", [])
clayPit = Card("gold", [["clay", "ore"]], 0, 0, 1, "Clay Pit", "brown", [])
timberYard = Card("gold", [["stone", "wood"]], 0, 0, 1, "Timber Yard", "brown", [])
westTradingPost = Card(0, 0, ["Forum"], "less g raw res left", 0, "West Trading Post", "yellow", [])
loom = Card(0, [["loom"]], 0, 0, 0, "Loom", "grey",[])
glassworks = Card(0, [["glass"]], 0, 0, 0, "Glass Works", "grey", [])
press = Card(0, [["papyrus"]], 0, 0, 0, "Press", "grey", [])
workshop = Card(["glass"], "cog", ["Laboratory"], 0, 0, "Workshop", "green", [])
barracks = Card(["ore"], "mp", 0, 0, 0, "Barracks", "red", [])
stockade = Card(["wood"], "mp", 0, 0, 0, "Stockade", "red", [])
guardTower = Card(["clay"], "mp", 0, 0, 0, "Guard Tower", "red", [])
apothecary = Card(["loom"], "compass", ["Stables", "Dispensary"], 0, 0, "Apothecary", "green", [])
scriptorium = Card(["papyrus"], "tablet", ["Courthouse", "Library"], 0, 0, "Scriptorium", "green", [])
eastTradingPost = Card(0, 0, ["Forum"], "less g raw res right", 0, "East Trading Post", "yellow", [])
marketplace = Card(0, 0, ["Caravansery"], "less g man res", 0, "Marketplace", "yellow", [])
baths = Card(["stone"], 3, ["Aqueduct"], 0, 0, "Baths", "blue", [])
theater = Card(0, 2, ["Statue"], 0, 0, "Theater", "blue", [])
stonePit = Card(0, [["stone"]], 0, 0, 0, "Stone Pit", "brown", [])
oreVein = Card(0, [["ore"]], 0, 0, 0, "Ore Vein", "brown", [])

cards1 = [oreVein, clayPool, lumberYard, altar, clayPit, timberYard, westTradingPost, loom, glassworks, press, workshop, barracks, stockade, guardTower, apothecary, scriptorium, eastTradingPost, marketplace, baths, theater, stonePit]

#Age 2 Cards
aqueduct = Card(["stone", "stone", "stone"], 5, 0, 0, 0, "Aqueduct", "blue", [])
archeryRange = Card(["wood", "wood", "ore"], "2mp", 0, 0, 0, "Archery Range", "red", [])
brickyard = Card("gold", [["clay"],["clay"]], 0, 0, 1, "Brickyard", "brown", [])
caravansery = Card(["wood", "wood"], 0, "lighthouse", "caravansery", 0, "Caravansery", "yellow", [])
courthouse = Card(["clay", "clay", "loom"], 4, 0, 0, 0, "Courthouse", "blue", [])
dispensary = Card(["ore", "ore", "glass"], "compass", ["Lodge", "Arena"], 0, 0, "Dispensary", "green", [])
forum = Card(["clay", "clay"], 0, ["Haven"], "forum", 0, "Forum", "yellow", [])
foundry = Card("gold", [["ore"], ["ore"]], 0, 0, 1, "Foundry", "brown", [])
glassworks = Card(0, [["glass"]], 0, 0, 0, "Glassworks", "grey", [])
laboratory = Card(["clay", "clay", "papyrus"], "cog", ["Observatory", "Siege Workshop"], 0, 0, "Laboratory", "green", [])
library = Card(["stone", "stone", "loom"], "tablet", ["Senate", "University"], 0, 0, "Library", "green", [])
loom = Card(0, [["loom"]], 0, 0, 0, "Loom", "grey", [])
press = Card(0, [["papyrus"]], 0, 0, 0, "Press", "grey", [])
quarry = Card("gold", [["stone"], ["stone"]], 0, 0, 1, "Quarry", "brown", [])
sawmill = Card("gold", [["wood"], ["wood"]], 0, 0, 1, "Sawmill", "brown", [])
school = Card(["wood", "papyrus"], "tablet", ["Academy", "Study"], 0, 0, "School", "green", [])
stables = Card(["clay", "wood", "ore"], "2mp", 0, 0, 0, "Stables", "red", [])
statue = Card(["ore", "ore", "wood"], 4, ["Gardens"], 0, 0, "Statue", "blue", [])
temple = Card(["wood", "clay", "glass"], 3, ["Pantheon"], 0, 0, "Temple", "blue", [])
vineyard = Card(0, 0, 0, "gold per brown card", 0, "Vineyard", "yellow", [])
walls = Card(["stone", "stone", "stone"], "2mp", ["Fortifications"], 0, 0, "Walls", "red", [])

cards2 = [aqueduct, archeryRange, brickyard, caravansery, courthouse, dispensary, forum, foundry, glassworks, laboratory, library, loom, press, quarry, sawmill, school, stables, statue, temple, vineyard, walls]

#Age 3 Cards
academy = Card(["stone", "stone", "stone", "glass"] , "compass", 0, 0, 0, "Academy", "green", [])
arena = Card(["stone", "stone", "ore"] , 0, "gold and vp per wonder stage", 0, 0, "Arena", "yellow", [])
arsenal = Card(["wood", "wood", "ore", "loom"] , "3mp", 0, 0, 0, "Arsenal", "red", [])
fortifications = Card(["ore", "ore", "ore", "stone"] , "3mp", 0, 0, 0, "Fortifications", "red", [])
gardens = Card(["clay", "clay", "wood"] , 5, 0, 0, 0, "Gardens", "blue", [])
haven = Card(["wood", "ore", "loom"] , 0, "gold and vp per brown card", 0, 0, "Haven", "yellow", [])
lighthouse = Card(["stone", "glass"] , 0, "gold and vp per yellow card", 0, 0, "Lighthouse", "yellow", [])
lodge = Card(["clay", "clay", "papyrus", "loom"] , "compass", 0, 0, 0, "Lodge", "green", [])
observatory = Card(["ore", "ore", "loom", "glass"] , "cog", 0, 0, 0, "Observatory", "green", [])
palace = Card(["stone", "ore", "wood", "clay", "glass", "papyrus", "loom"] , 8, 0, 0, 0, "Palace", "blue", [])
pantheon = Card(["clay", "clay", "ore", "glass", "papyrus", "loom"] , 7, 0, 0, 0, "Pantheon", "blue", [])
senate = Card(["wood", "wood", "stone", "ore"] , 6, 0, 0, 0, "Senate", "blue", [])
seigeWorkshop = Card(["clay", "clay", "clay", "wood"] , "3mp", 0, 0, 0, "Seige Workshop", "red", [])
study = Card(["wood", "papyrus", "loom"] , "cog", 0, 0, 0, "Study", "green", [])
townHall = Card(["stone", "stone", "ore", "glass"] , 6, 0, 0, 0, "Town Hall", "blue", [])
university = Card(["wood", "wood", "papyrus", "glass"] , "tablet", 0, 0, 0, "University", "green", [])

cards3 = [academy, arena, arsenal, fortifications, gardens, haven, lighthouse, lodge, observatory, palace, pantheon, senate, seigeWorkshop, study, townHall, university]

#Guilds

buildersGuild = Card(["stone", "stone", "clay", "clay", "glass"] , 0, 0, 0, 0, "Builders Guild", "purple", [])
craftsmensGuild = Card(["stone", "stone", "ore", "ore"] , 0, 0, 0, 0, "Craftsmens Guild", "purple", [])
magistratesGuild = Card(["wood", "wood", "wood", "stone", "loom"] , 0, 0, 0, 0, "Magistrates Guild", "purple", [])
philosophersGuild = Card(["clay", "clay", "clay", "papyrus", "loom"] , 0, 0, 0, 0, "Philosophers Guild", "purple", [])
scientistsGuild = Card(["wood", "wood", "ore", "ore", "papyrus"] , 0, "science", 0, 0, "Scientists Guild", "purple", [])
shipownersGuild = Card(["wood", "wood", "wood", "glass", "papyrus"] , 0, 0, 0, 0, "Shipowners Guild", "purple", [])
spiesGuild = Card(["clay", "clay", "clay", "glass"] , 0, 0, 0, 0, "Spies Guild", "purple", [])
strategistsGuild = Card(["ore", "ore", "stone", "loom"] , 0, 0, 0, 0, "Strategists Guild", "purple", [])
tradersGuild = Card(["glass", "loom", "papyrus"] , 0, 0, 0, 0, "Traders Guild", "purple", [])
workersGuild = Card(["ore", "ore", "clay", "stone", "wood"] , 0, 0, 0, 0, "Workers Guild", "purple", [])

guilds = [buildersGuild, craftsmensGuild, magistratesGuild, philosophersGuild, scientistsGuild, shipownersGuild, spiesGuild, strategistsGuild, tradersGuild, workersGuild]

#wonders
#Things to fix (maybe), Rhodos MP is always 2 doesnt depend on age, epheseos gives gold, one out of 3 science
alexandriaA = Wonder("Alexandria A", ["glass"], Card(["stone", "stone"], 3, 0, 0, 0, "Stage 1", "wonder", []), Card(["ore", "ore"], 0, 0, "caravansery", 0, "Stage 2", "wonder", []), Card(["glass", "glass"], 7, 0, 0, 0, "Stage 3", "wonder", []))
halikarnassosA = Wonder("Halikarnassos A", ["loom"], Card(["clay", "clay"], 3, 0, 0, 0, "Stage 1", "wonder", []), Card(["ore", "ore", "ore"], 0, 0, "pick discarded", 0, "Stage 2", "wonder", []), Card(["loom", "loom"], 7, 0, 0, 0, "Stage 3", "wonder", []))
gizahA = Wonder("Gizah A", ["stone"], Card(["stone", "stone"], 3, 0, 0, 0, "Stage 1", "wonder", []), Card(["wood", "wood", "wood"], 5, 0, 0, 0, "Stage 2", "wonder", []), Card(["stone", "stone", "stone", "stone"], 7, 0, 0, 0, "Stage 3", "wonder", []))
olympiaA = Wonder("Olympia A", ["wood"], Card(["wood", "wood"], 3, 0, 0, 0, "Stage 1", "wonder", []), Card(["stone", "stone"], 0, 0, "free card", 0, "Stage 2", "wonder", []), Card(["ore", "ore"], 7, 0, 0, 0, "Stage 3", "wonder", []))
ephesosA = Wonder("Ephesos A", ["papyrus"], Card(["stone", "stone"], 3, 0, 0, 0, "Stage 1", "wonder", []), Card(["wood", "wood"], "9g", 0, 0, 0, "Stage 2", "wonder", []), Card(["papyrus", "papyrus"], 7, 0, 0, 0, "Stage 3", "wonder", []))
babylonA = Wonder("Babylon A", ["clay"], Card(["clay", "clay"], 3, 0, 0, 0, "Stage 1", "wonder", []), Card(["wood", "wood", "wood"], 0, 0, "science", 0, "Stage 2", "wonder", []), Card(["clay", "clay", "clay", "clay"], 7, 0, 0, 0, "Stage 3", "wonder", []))
rhodosA = Wonder("Rhodos A", ["ore"], Card(["wood", "wood"], 3, 0, 0, 0, "Stage 1", "wonder", []), Card(["clay", "clay", "clay"], "2mp", 0, 0, 0, "Stage 2", "wonder", []), Card(["ore", "ore", "ore", "ore"], 7, 0, 0, 0, "Stage 3", "wonder", []))

wonders = [alexandriaA, halikarnassosA, gizahA, olympiaA, ephesosA, babylonA, rhodosA]

#ai
#First three values correspond to gold piece value in ages 1,2,3 respectively
#Fourth value is science focus three options 0=almost never takes science, 0.5 = normal science rules apply, 1=Always takes science if possible, not a scale only these values apply
#Fifth value is military focus
goldFourty = ai(0.4,0.4,0.4,0.5,1)
goldThirtyThree = ai(0.3333,0.3333,0.3333,0.5,1)
goldFifty = ai(0.5,0.5,0.5,0.5,1)
goldVariable = ai(0.5,0.5,0.3,0.5,1)

class GameState:
    def __init__(self):
        pass
    def startState():
        for i in cards3:
            if i.colour == "purple":
                cards3.remove(i)
        random.shuffle(wonders)
        random.shuffle(cards1)  
        random.shuffle(cards2)
        random.shuffle(guilds)
        for i in range(5):
            cards3.append(guilds[i])
        random.shuffle(cards3)
        
        
def playGame():
    GameState.startState()
    turn = 1
    age = 1
    discardPile = []
    while age <= 3:
        if turn == 1 and age == 1:
            player1 = Player(wonders[0], 3, [], [], 0, 0, [], [], "AI Player 1", [], [], goldFifty)
            player2 = Player(wonders[1], 3, [], [], 0, 0, [], [], "Human Player 2", [], [], goldFifty)
            player3 = Player(wonders[2], 3, [], [], 0, 0, [], [], "AI Player 3", [], [], goldFifty)
            players = [player1, player2, player3]
            
            for player in players:
                player.hand.append(player.wonder.stage1)
            
            
            for i in range(3):
                players[i].resources.append(players[i].wonder.resource) #give player their wonders starting resource
        if turn == 1:
            if age == 1:        
                for i in range(3):
                    for j in range(7):
                        players[i].hand.append(cards1[i*7 + j]) #give players thier starting hands
            elif age == 2:        
                for i in range(3):
                    for j in range(7):
                        players[i].hand.append(cards2[i*7 + j]) #give players thier starting hands
            elif age == 3:        
                for i in range(3):
                    for j in range(7):
                        players[i].hand.append(cards3[i*7 + j]) #give players thier starting hands
        
        #while turn < 7:
        if turn != 1:
            wonderCopy = [0,0,0]
            for i in range(3):
                for j in players[i].hand:
                    if j.colour == "wonder":
                        wonderCopy[i] = j
                        players[i].hand.remove(j)
            if age == 1 or age == 3:
                handCopy = players[0].hand
                players[0].hand = players[1].hand
                players[1].hand = players[2].hand
                players[2].hand = handCopy
            elif age == 2:
                handCopy = players[0].hand
                players[0].hand = players[2].hand
                players[2].hand = players[1].hand
                players[1].hand = handCopy
            for i in range(3):
                if wonderCopy[i] != 0:
                    players[i].hand.append(wonderCopy[i])
        
        buildingChoice = []
        
        for i in range(3): #FIX to 3
            
            print(players[i].resources)
            playableCards = isHandPlayable(players, i)
            
            print(players[i].name + "'s Turn")
            print("Your wonder is " + players[i].wonder.name)
            print("You have " + str(players[i].gold) + " gold")
            print("Your current victory points are: " + str(players[i].vp))
            print("Your military losses are: " + str(players[i].effects.count("loss")))
            print("-------------------------------------------------------------")
            print("Your currently built buildings are: ")
            for k in players[i].buildings:
                print(k.name + " " + k.colour)
            print()
            print("Cards playable for free or from own resources:")
            for k in playableCards:
                if k.neighbourPay == [] and k.colour != "wonder":
                    print(k.name)
            print()
            
            print("Cards playable from trade:")
            for k in playableCards:
                if k.neighbourPay != [] and k.colour != "wonder":
                    neighbourPayDistribution = ""
                    for j in k.neighbourPay:
                        if neighbourPayDistribution != "":
                            neighbourPayDistribution += "or "
                        for l in range(3):
                            if j[l] != []:
                                neighbourPayDistribution += "Pay " + players[l].name + " " + str(j[l]) + " gold "
                                    
                    print(k.name + ". " + neighbourPayDistribution)
            print()
            
            print("Unplayable cards:")
            for k in players[i].hand:
                if k not in playableCards and k.colour != "wonder":
                    print(k.name)
            print()
            
            if "completed wonder" in players[i].effects:
                print("Your wonder is already completed")
            else:
                for k in players[i].hand:
                    if k in playableCards and k.colour == "wonder" and k.neighbourPay == []:
                        print(k.name + " of your wonder is playable from own resources.")
                    elif k in playableCards and k.colour == "wonder" and k.neighbourPay != []:
                        print(k.name + " of your wonder is playable from trade.")
                        neighbourPayDistribution = ""
                        for j in k.neighbourPay:
                            if neighbourPayDistribution != "":
                                neighbourPayDistribution += "or "
                            for l in range(3):
                                if j[l] != []:
                                    neighbourPayDistribution += "Pay " + players[l].name + " " + str(j[l]) + " gold "
                    elif k not in playableCards and k.colour == "wonder":
                        print(k.name + " of your wonder is unplayable.")
                print()
            if players[i].ai == "human":
                chosenCard = "blank"
                while chosenCard == "blank":
                    choice = chooseAction(players, i)
                    if choice == "1":
                        chosenCard = "blank"
                        while chosenCard == "blank":
                            builder = input("Type the name of the structure you'd like to build exactly as it appears: ")
                            for k in playableCards:
                                if k.name == builder:
                                    chosenCard = k
                                    break
                        buildingChoice.append([1,chosenCard])
                    elif choice == "2":
                        chosenCard = "blank"
                        discardChoice = "blank"
                        for k in playableCards:
                            if k.colour == "wonder":
                                chosenCard = k
                        if chosenCard == "blank":
                            print("Your wonder stage is unplayable!")
                            continue
                        while discardChoice == "blank":
                            wonderChoice = input("Choose a card from your hand to place under your board: ")
                            for k in players[i].hand:
                                if k.name == wonderChoice:
                                    discardChoice = k
                                
                        buildingChoice.append([2, chosenCard, discardChoice])
                    elif choice == "3":
                        chosenCard = "blank"
                        while chosenCard == "blank":
                            builder = input("Type the name of the structure you'd like to discard exactly as it appears: ")
                            for k in players[i].hand:
                                if k.name == builder and k.colour != "wonder":
                                    chosenCard = k
                                    break
                        buildingChoice.append([3,chosenCard])
                    elif choice == "4":
                        chosenCard = "blank"
                        while chosenCard == "blank":
                            builder = input("Type the name of the structure you'd like to build for free exactly as it appears: ")
                            for k in players[i].hand:
                                if k.name == builder:
                                    chosenCard = k
                                    chosenCard.neighbourPay = []
                                    players[i].effects.remove("free card age")
                                    break
                        buildingChoice.append([1,chosenCard])
            else:
                playList = aiHeuristicEval(players, playableCards, i, age, players[i].hand, discardPile)
                aiChooseAction(playList, players, i, playableCards, age, 0, buildingChoice, discardPile)
            print("-------------------------------------------------------------")   
        
        playerCounter = 0
        for x in buildingChoice:
            if x[0] == 1:
                buildStructure(x[1], playerCounter, players, buildingChoice)
            if x[0] == 2:
                buildWonderStage(x[1], playerCounter, players, discardPile, x[2], age, buildingChoice)
            if x[0] == 3:
                discardCard(x[1], discardPile, players, playerCounter)
            playerCounter += 1
                
        
        if turn == 6:
            if age == 1: #Calculates war at end of age
                for i in range(3):
                    if players[i].mpower > players[i-1].mpower:
                        players[i].vp += 1
                        players[i-1].effects.append("loss")
                        players[i-1].vp -= 1
                    elif players[i].mpower < players[i-1].mpower:
                        players[i].effects.append("loss")
                        players[i].vp -= 1
                        players[i-1].vp += 1
            if age == 2:
                for i in range(3):
                    if players[i].mpower > players[i-1].mpower:
                        players[i].vp += 3
                        players[i-1].effects.append("loss")
                        players[i-1].vp -= 1
                    elif players[i].mpower < players[i-1].mpower:
                        players[i].effects.append("loss")
                        players[i].vp -= 1
                        players[i-1].vp += 3
            if age == 3:
                for i in range(3):
                    if players[i].mpower > players[i-1].mpower:
                        players[i].vp += 5
                        players[i-1].effects.append("loss")
                        players[i-1].vp -= 1
                    elif players[i].mpower < players[i-1].mpower:
                        players[i].effects.append("loss")
                        players[i].vp -= 1
                        players[i-1].vp += 5
                vpFinal = calculateVictoryPoints(players)
                for i in range(3):
                    print(players[i].name + " scored " + str(vpFinal[i]))
                print(players[vpFinal.index(max(vpFinal))].name + " has won!")
                return(players[0].name, players[1].name, players[2].name, vpFinal)
           
            for i in players: #Discards final card in hand
                for j in i.hand:
                    if j.colour != "wonder":
                        j.neighbourPay = []
                        discardPile.append(j)
                        i.hand.remove(j)
            
            for i in players:
                if "free card" in i.effects and "free card age" not in i.effects:
                    i.effects.append("free card age")
            
            turn = 1
            age += 1
            continue
        #input()
        turn += 1
            
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
    #print("These are the final states")
    #print(finalStates)
    return [s[0] for s in finalStates]

#Given list of need and list of resource baskets, returns each way ONE given need
#is resolved by ONE given basket. Therefore returns a list of states with one less
#need and one less basket.
        
def resolveNeed(needs, resources):
    resolutions = []
    for need in needs:
        for basket in resources:
            if need in basket:
                otherNeeds = needs.copy()
                otherNeeds.remove(need)
                otherResources = resources.copy()
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

def isHandPlayable(players, i):
    playableCards = []
    natResLeftMulti = 2
    natResRightMulti = 2
    refResMulti = 2
    if "less g raw res left" in players[i].effects:
        natResLeftMulti = 1
    if "less g raw res right" in players[i].effects:
        natResRightMulti = 1
    if "less g man res" in players[i].effects:
        refResMulti = 1
    neighbourPayList = [[],[],[]] #For calculating neighbour pay each empty list inside the list relates to player1,2,3 respectively
    if "caravansery" in players[i].effects: #As the resources from gold cards aren't tradeable they are added here so other players wont make use of them
        players[i].resources.append(["wood", "stone", "ore", "clay"])
        if players[i].effects.count("caravansery") == 2:
            players[i].resources.append(["wood", "stone", "ore", "clay"])
    if "forum" in players[i].effects:
        players[i].resources.append(["glass", "loom", "papyrus"])
    for j in range(len(players[i].hand)):
        players[i].hand[j].neighbourPay = []
        if players[i].hand[j].cost == 0: #If card is free
            playableCards.append(players[i].hand[j])
        elif players[i].hand[j].cost == "gold" and players[i].gold >= players[i].hand[j].goldCost: #If card costs gold and player can afford
            playableCards.append(players[i].hand[j])
        elif players[i].hand[j].cost == "gold":
            continue
        elif players[i].hand[j].name in players[i].chains:
            playableCards.append(players[i].hand[j])
        else: #Goes to check needs and baskets
            needs = players[i].hand[j].cost
            resources = players[i].resources
            resolvedNeeds = resolveNeeds(needs, resources)
            if resolvedNeeds == [[]]: #If needs are resolved from own resources
                playableCards.append(players[i].hand[j])
            else: #Check with neighbours resources
                for k in range(3):
                    if k == i: #Stops program from checking against own resources again
                        continue
                    else:
                        for needs in resolvedNeeds: #Cycles through possible needed resource packs
                            neighbourResolvedNeeds = resolveNeeds(needs, players[k].resources)
                            resolvedNeedsNat = needs.count('wood') + needs.count('clay') + needs.count('stone') + needs.count('ore') #Counts number of unresolved natural needs in this paticular needs group after own players resources used
                            resolvedNeedsRef = needs.count('glass') + needs.count('papyrus') + needs.count('loom') #Same but for refined
                            
                            if neighbourResolvedNeeds == resolvedNeeds: #If first neighbour doesn't resolve anymore needs continues so that if second neighbour resolves all needs won't add that card twice
                                continue
                            elif neighbourResolvedNeeds == [[]]:
                                if players[i-1] == players[k]:
                                    neighbourPayList[k] = resolvedNeedsNat*natResLeftMulti + resolvedNeedsRef*refResMulti #Adds to the list the number of unresolved nat and refined resources resolved by this neighbour into corresponding 123 slot in list
                                elif players[i-2] == players[k]:
                                    neighbourPayList[k] = resolvedNeedsNat*natResRightMulti + resolvedNeedsRef*refResMulti
                                else:
                                    print("Broken in first neighbour pay")
                                    exit
                                if players[i].hand[j] not in playableCards and neighbourPayList[k] <= players[i].gold: #As multiple unresolved needs blocks get queried this makes it still add a new way of paying for resource without adding card to playable cards again
                                    playableCards.append(players[i].hand[j])
                                players[i].hand[j].neighbourPay.append(neighbourPayList)
                                neighbourPayList = [[],[],[]]
                            else:
                                for l in range(3): #If first person doesn't resolve needs then checks again with new resource lists
                                    if l == k or l == i:
                                        continue
                                    else:
                                        for neighbourNeeds in neighbourResolvedNeeds:
                                            neighbour2ResolvedNeeds = resolveNeeds(neighbourNeeds, players[l].resources)
                                            resolvedNeedsNatNeighbour = neighbourNeeds.count(['wood']) + neighbourNeeds.count(['clay']) + neighbourNeeds.count(['stone']) + neighbourNeeds.count(['ore'])
                                            resolvedNeedsRefNeighbour = neighbourNeeds.count(['glass']) + neighbourNeeds.count(['papyrus']) + neighbourNeeds.count(['loom'])

                                            if neighbour2ResolvedNeeds == [[]]:
                                                if players[i-1] == players[k]:
                                                    neighbourPayList[k] = (resolvedNeedsNat - resolvedNeedsNatNeighbour)*natResLeftMulti + (resolvedNeedsRef - resolvedNeedsRefNeighbour)*refResMulti
                                                    neighbourPayList[l] = (resolvedNeedsNatNeighbour*natResRightMulti) + (resolvedNeedsRefNeighbour*refResMulti)
                                                    
                                                elif players[i-2] == players[k]:
                                                    neighbourPayList[k] = (resolvedNeedsNat - resolvedNeedsNatNeighbour)*natResRightMulti + (resolvedNeedsRef - resolvedNeedsRefNeighbour)*refResMulti
                                                    neighbourPayList[l] = (resolvedNeedsNatNeighbour*natResLeftMulti) + (resolvedNeedsRefNeighbour*refResMulti)
                                                else:
                                                    print("Broken in neighbour pay")
                                                    quit
                                                if neighbourPayList[k] + neighbourPayList[l] <= players[i].gold and players[i].hand[j] not in playableCards:
                                                    playableCards.append(players[i].hand[j])
                                                    players[i].hand[j].neighbourPay.append(neighbourPayList)
                                                neighbourPayList = [[],[],[]]
    if "caravansery" in players[i].effects:
        players[i].resources.remove(["wood", "stone", "ore", "clay"])
        if players[i].effects.count("caravansery") == 2:
            players[i].resources.remove(["wood", "stone", "ore", "clay"])
    if "forum" in players[i].effects:
        players[i].resources.remove(["glass", "loom", "papyrus"])
    
    return playableCards

def chooseAction(players, i):
    choice = 0
    if "free card age" in players[i].effects:
        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print("Would you like to:")
            print("1: Build a structure")
            print("2: Build your wonder stage")
            print("3: Discard a card for 3 gold")
            print("4: Build a structure for free this age")
            choice = input("Select your choice: ")
    else:
        while choice != "1" and choice != "2" and choice != "3":
            print("Would you like to:")
            print("1: Build a structure")
            print("2: Build your wonder stage")
            print("3: Discard a card for 3 gold")
            choice = input("Select your choice: ")
    return choice

def buildStructure(chosenCard, i, players, buildingChoice):
    if len(chosenCard.neighbourPay) == 1:
        moneySpent = 0
        for j in range(3):
            if chosenCard.neighbourPay[0][j] != []:
                players[j].gold += chosenCard.neighbourPay[0][j]
                moneySpent += chosenCard.neighbourPay[0][j]
        players[i].gold -= moneySpent
    elif len(chosenCard.neighbourPay) > 1:
        paymentChoice = -1
        moneySpent = 0
        whoPay = []
        while paymentChoice < 0 or paymentChoice > len(chosenCard.neighbourPay):
            for j in chosenCard.neighbourPay:
                paymentTotal = 0
                for k in j:
                    if k != []:
                        paymentTotal += k
                whoPay.append(paymentTotal)
            if whoPay.count(min(whoPay)) == 1:
                paymentChoice = whoPay.index(min(whoPay))
            else:
                while whoPay[paymentChoice] != min(whoPay) or paymentChoice == -1:
                    paymentChoice = random.randint(0,len(chosenCard.neighbourPay)-1)
        print(chosenCard.neighbourPay)
        print(paymentChoice)
        for j in range(3):
            if type(chosenCard.neighbourPay[paymentChoice][j]) == int:
                players[j].gold += chosenCard.neighbourPay[paymentChoice][j]
                moneySpent += chosenCard.neighbourPay[paymentChoice][j]
        players[i].gold -= moneySpent
        
    players[i].buildings.append(chosenCard)
    players[i].effects.append(chosenCard.colour)
    
    if type(chosenCard.produce) == int and chosenCard.produce != 0:
        players[i].vp += chosenCard.produce
    elif chosenCard.produce == "mp":
        players[i].mpower += 1
    elif chosenCard.produce == "2mp":
        players[i].mpower += 2
    elif chosenCard.produce == "3mp":
        players[i].mpower += 3
    elif chosenCard.produce == "cog" or chosenCard.produce == "compass" or chosenCard.produce == "tablet":
        players[i].science.append(chosenCard.produce)
    elif chosenCard.produce != 0:
        for k in chosenCard.produce:
            players[i].resources.append(k)
    
    if chosenCard.chain != 0:
        for k in chosenCard.chain:
            players[i].chains.append(chosenCard.chain)
    
    if chosenCard.effect != 0:
        players[i].effects.append(chosenCard.effect)
    if chosenCard.effect == "gold per brown card":
        players[i].gold += players[i].effects.count("brown") + players[i-1].effects.count("brown") + players[i-2].effects.count("brown")
        if i == 0:
            if buildingChoice[1][1].colour == "brown":
                players[i].gold += 1
            if buildingChoice[2][1].colour == "brown":
                players[i].gold += 1
        if i== 1:
            if buildingChoice[2][1].colour == "brown":
                players[i].gold += 1
    elif chosenCard.effect == "gold and vp per brown card":
        players[i].gold += players[i].effects.count("brown")
        if i == 0:
            if buildingChoice[1][1].colour == "brown":
                players[i].gold += 1
            if buildingChoice[2][1].colour == "brown":
                players[i].gold += 1
        if i== 1:
            if buildingChoice[2][1].colour == "brown":
                players[i].gold += 1
    elif chosenCard.effect == "gold and vp per yellow card":
        players[i].gold += players[i].effects.count("yellow")
        if i == 0:
            if buildingChoice[1][1].colour == "yellow":
                players[i].gold += 1
            if buildingChoice[2][1].colour == "yellow":
                players[i].gold += 1
        if i== 1:
            if buildingChoice[2][1].colour == "yellow":
                players[i].gold += 1
    elif chosenCard.effect == "gold and vp per wonder stage":
        players[i].gold += 3 * players[i].effect.count("wonder")
        if i == 0:
            if buildingChoice[1][1].colour == "wonder":
                players[i].gold += 3
            if buildingChoice[2][1].colour == "wonder":
                players[i].gold += 3
        if i== 1:
            if buildingChoice[2][1].colour == "wonder":
                players[i].gold += 3
    
    if chosenCard in players[i].hand:
        players[i].hand.remove(chosenCard)

def buildWonderStage(chosenCard, i, players, discardPile, discardChoice, age, buildingChoice):
    if len(chosenCard.neighbourPay) == 1:
        moneySpent = 0
        for j in range(3):
            if type(chosenCard.neighbourPay[0][j]) == int:
                players[j].gold += chosenCard.neighbourPay[0][j]
                moneySpent += chosenCard.neighbourPay[0][j]
                players[i].gold -= moneySpent
    elif len(chosenCard.neighbourPay) > 1:
        paymentChoice = -1
        moneySpent = 0
        whoPay = []
        while paymentChoice < 0 or paymentChoice > len(chosenCard.neighbourPay):
            for j in chosenCard.neighbourPay:
                paymentTotal = 0
                for k in j:
                    if k != []:
                        paymentTotal += k
                whoPay.append(paymentTotal)

            if whoPay.count(min(whoPay)) == 1:
                paymentChoice = whoPay.index(min(whoPay))
            else:
                while whoPay[paymentChoice] != min(whoPay) or paymentChoice == -1:
                    paymentChoice = random.randint(0,len(chosenCard.neighbourPay)-1)
                    
        for j in range(3):
            if type(chosenCard.neighbourPay[paymentChoice][j]) == int:
                players[j].gold += chosenCard.neighbourPay[paymentChoice][j]
                moneySpent += chosenCard.neighbourPay[paymentChoice][j]
        players[i].gold -= moneySpent
    
    players[i].buildings.append(chosenCard)
    players[i].effects.append(chosenCard.colour)
    
    if chosenCard.effect != 0:
        players[i].effects.append(chosenCard.effect)

    if chosenCard.effect == "pick discarded":
        if players[i].ai == "human":
            discardPick = -1
            for k in discardPile:
                print(k.name)
            while discardPick <= -1 or discardPick >= len(discardPile):
                print(discardPile)
                print(len(discardPile))
                discardPick = input("Pick a discarded card to build: ")
                discardPick = int(discardPick)
                print(discardPick)
            buildStructure(discardPile[discardPick], i, players, buildingChoice)
        else:
            pickDiscardedHandCopy = players[i].hand
            players[i].hand = discardPile
            playableCards = isHandPlayable(players, i)
            playList = aiHeuristicEval(players, playableCards, i, age, players[i].hand, discardPile)
            aiChooseAction(playList, players, i, playableCards, age, 1, buildingChoice, discardPile)
            players[i].hand = pickDiscardedHandCopy
    elif chosenCard.effect == "free card":
        players[i].effects.append("free card age")
    
    if type(chosenCard.produce) == int and chosenCard.produce != 0:
        players[i].vp += chosenCard.produce
    elif chosenCard.produce == "2mp":
        players[i].mpower += 2
    elif chosenCard.produce == "9g":
        players[i].gold += 9
    elif chosenCard.produce != 0:
        for k in chosenCard.produce:
            players[i].resources.append(k)
    
    
    if(chosenCard.name == "Stage 1"):
        for k in players[i].hand:
            if k.colour == "wonder":
                players[i].hand.remove(k)
        players[i].hand.append(players[i].wonder.stage2)
    elif(chosenCard.name == "Stage 2"):
        for k in players[i].hand:
            if k.colour == "wonder":
                players[i].hand.remove(k)
        players[i].hand.append(players[i].wonder.stage3)
    elif(chosenCard.name == "Stage 3"):
        for k in players[i].hand:
            if k.colour == "wonder":
                players[i].hand.remove(k)
        players[i].effects.append("completed wonder")
    players[i].hand.remove(discardChoice)

def calculateVictoryPoints(players):
    vpCounter = [players[0].vp, players[1].vp, players[2].vp]
    for i in range(3):
        vpCounter[i] += players[i].gold %3
        vpCounter[i] += techVictoryPoints(players[i].science.count("cog"), players[i].science.count("tablet"), players[i].science.count("compass"), players[i].effects.count("science"))
        if spiesGuild in players[i].buildings:
            vpCounter[i] += players[i-1].effects.count("red") + players[i-2].effects.count("red")
        if magistratesGuild in players[i].buildings:
            vpCounter[i] += players[i-1].effects.count("blue") + players[i-2].effects.count("blue")
        if workersGuild in players[i].buildings:
            vpCounter[i] += players[i-1].effects.count("brown") + players[i-2].effects.count("brown")
        if craftsmensGuild in players[i].buildings:
            vpCounter[i] += (players[i-1].effects.count("grey") + players[i-2].effects.count("grey")) * 2
        if tradersGuild in players[i].buildings:
            vpCounter[i] += players[i-1].effects.count("yellow") + players[i-2].effects.count("yellow")
        if philosophersGuild in players[i].buildings:
            vpCounter[i] += players[i-1].effects.count("green") + players[i-2].effects.count("green")
        if buildersGuild in players[i].buildings:
            vpCounter[i] += players[i-1].effects.count("wonder") + players[i-2].effects.count("wonder") + players[i].effects.count("wonder")
        if shipownersGuild in players[i].buildings:
            vpCounter[i] += players[i].effects.count("brown") + players[i].effects.count("grey") + players[i].effects.count("purple")
        if philosophersGuild in players[i].buildings:
            vpCounter[i] += players[i-1].effects.count("loss") + players[i-2].effects.count("loss")  
        if haven in players[i].buildings:
            vpCounter[i] += players[i].effects.count("brown")
        if lighthouse in players[i].buildings:
            vpCounter[i] += players[i].effects.count("yellow")
        if arena in players[i].buildings:
            vpCounter[i] += players[i].effects.count("wonder")
    return vpCounter
        
def techVictoryPoints(cogs, tablets, compasses, wilds ):
    if wilds == 0:
        return noWildsTechPoints(cogs, tablets, compasses)
    if wilds == 1:
        return max( noWildsTechPoints( cogs+1, tablets, compasses ),
                    noWildsTechPoints( cogs, tablets+1, compasses ),
                    noWildsTechPoints( cogs, tablets, compasses+1) 
                  )
    if wilds == 2:
        return max( noWildsTechPoints( cogs+2, tablets, compasses ),
                    noWildsTechPoints( cogs, tablets+2, compasses ),
                    noWildsTechPoints( cogs, tablets, compasses+2),
                    noWildsTechPoints( cogs+1, tablets+1, compasses ),
                    noWildsTechPoints( cogs+1, tablets, compasses+1 ),
                    noWildsTechPoints( cogs, tablets+1, compasses+1) 
                  )

def noWildsTechPoints(cogs, tablets, compasses):
    return ( cogs**2 + tablets**2 + compasses**2 + 7 * min(cogs,tablets,compasses))

def discardCard(chosenCard, discardPile, players, i):
    chosenCard.neighbourPay = []
    discardPile.append(chosenCard)
    players[i].hand.remove(chosenCard)
    players[i].gold += 3
    
def aiChooseAction(playList, players, i, playableCards, age, discardYes, buildingChoice, discardPile):
    choiceChosen = 0
    discardChoice = 0
    wonderBuilt = 0
    wonderCopy = 0
    while choiceChosen == 0:
        if max(playList) < 1:
            for k in players[i].hand:
                if k.colour == "wonder":
                    wonderCopy = k
                    players[i].hand.remove(k)
            if calculateVictoryPoints(players)[i-2] > calculateVictoryPoints(players)[i-1]:
                if i < 2:
                    discardList = aiHeuristicEval(players, playableCards, i+1, age, players[i].hand, discardPile)
                    discardChoice = players[i].hand[discardList.index(max(discardList))]
                else:
                    discardList = aiHeuristicEval(players, playableCards, 0, age, players[i].hand, discardPile)
                    discardChoice = players[i].hand[discardList.index(max(discardList))]
            else:
                if i > 0:
                    discardList = aiHeuristicEval(players, playableCards, i-1, age, players[i].hand, discardPile)
                    discardChoice = players[i].hand[discardList.index(max(discardList))]
                else:
                    discardList = aiHeuristicEval(players, playableCards, i-1, age, players[i].hand, discardPile)
                    discardChoice = players[i].hand[discardList.index(max(discardList))]
            choiceChosen = 1
            if wonderCopy != 0:
                players[i].hand.append(wonderCopy)
        elif players[i].hand[playList.index(max(playList))] in playableCards:
            if players[i].hand[playList.index(max(playList))].colour == "wonder":
                if calculateVictoryPoints(players)[i-2] > calculateVictoryPoints(players)[i-1]:
                    if i < 2:
                        discardList = aiHeuristicEval(players, playableCards, i+1, age, players[i].hand, discardPile)
                        for k in players[i].hand:
                            if k.colour == "wonder":
                                discardList[players[i].hand.index(k)] = -100
                        discardChoice = players[i].hand[discardList.index(max(discardList))]
                    else:
                        discardList = aiHeuristicEval(players, playableCards, 0, age, players[i].hand, discardPile)
                        for k in players[i].hand:
                            if k.colour == "wonder":
                                discardList[players[i].hand.index(k)] = -100
                        discardChoice = players[i].hand[discardList.index(max(discardList))]
                else:
                    if i > 0:
                        discardList = aiHeuristicEval(players, playableCards, i-1, age, players[i].hand, discardPile)
                        for k in players[i].hand:
                            if k.colour == "wonder":
                                discardList[players[i].hand.index(k)] = -100
                        discardChoice = players[i].hand[discardList.index(max(discardList))]
                    else:
                        discardList = aiHeuristicEval(players, playableCards, i-1, age, players[i].hand, discardPile)
                        for k in players[i].hand:
                            if k.colour == "wonder":
                                discardList[players[i].hand.index(k)] = -100
                        discardChoice = players[i].hand[discardList.index(max(discardList))]
                choiceChosen = 1
                wonderBuilt = 1
            else:
                choiceChosen = 1
        else:
            playList[playList.index(max(playList))] = -1
    if discardYes == 0:
        if discardChoice == 0:
            print("Built: " + players[i].hand[playList.index(max(playList))].name)
            buildingChoice.append([1,players[i].hand[playList.index(max(playList))]])
        elif wonderBuilt == 1:
            print("Built wonder and discarded " + discardChoice.name)
            buildingChoice.append([2, players[i].hand[playList.index(max(playList))], discardChoice])
        else:
            print("Discarded " + discardChoice.name)
            buildingChoice.append([3, discardChoice])
    elif discardYes == 1:
        if discardChoice == 0:
            print("Built: " + players[i].hand[playList.index(max(playList))].name)
            buildStructure(players[i].hand[playList.index(max(playList))], i, players, buildingChoice)
        else:
            print("Discarded " + discardChoice.name)
            discardCard(discardChoice, discardPile, players, i)

def aiHeuristicEval(players, playableCards, i, age, hand, discardPile):
    heuristicEval = []
    cardCost = 0
    if type(players[i].ai) != str:
        if age == 1:
            goldValue = players[i].ai.goldValue1
        if age == 2:
            goldValue = players[i].ai.goldValue2
        if age == 3:
            goldValue = players[i].ai.goldValue3
    else:
        goldValue = 0.3333
    if players[i].ai == "random":
        heuristicEval = [random.randrange(1,100,1) for j in hand]
    else:
        for j in hand:
            cardCost = j.goldCost
            if j.neighbourPay != []:
                cardCostChoice = []
                for k in j.neighbourPay:
                    cardCostCounter = 0
                    for l in k:
                        if type(l) == int:
                            cardCostCounter += l
                    cardCostChoice.append(cardCostCounter)
                cardCost += min(cardCostChoice)
            if j.colour == "blue":
                heuristicEval.append(j.produce - (cardCost*goldValue))
            
            elif j.colour == "red":
                if players[i-1].mpower + age > players[i].mpower or players[i-2].mpower + age > players[i].mpower:
                    heuristicEval.append(6 - (cardCost*goldValue)) #FIX
                elif players[i-1].mpower + age >= players[i].mpower or players[i-2].mpower + age >= players[i].mpower:
                    heuristicEval.append(4 - (cardCost*goldValue))
                else:
                    heuristicEval.append((2 - (cardCost*goldValue))*players[i].ai.militaryFocus)
            
            elif j.colour == "green" and players[i].ai.scienceFocus == 0.5:
                if players[i].science.count("cog") + players[i].science.count("compass") + players[i].science.count("tablet") == 0:
                    heuristicEval.append(5 - (cardCost*goldValue))
                elif age == 1:
                    heuristicEval.append(3 - (cardCost*goldValue))
                else:
                    if j.produce == "cog":
                        scienceDifference = techVictoryPoints(players[i].science.count("cog")+1, players[i].science.count("tablet"), players[i].science.count("compass"), players[i].effects.count("science")) - techVictoryPoints(players[i].science.count("cog"), players[i].science.count("tablet"), players[i].science.count("compass"), players[i].effects.count("science"))
                    elif j.produce == "tablet":
                        scienceDifference = techVictoryPoints(players[i].science.count("cog"), players[i].science.count("tablet")+1, players[i].science.count("compass"), players[i].effects.count("science")) - techVictoryPoints(players[i].science.count("cog"), players[i].science.count("tablet"), players[i].science.count("compass"), players[i].effects.count("science"))
                    elif j.produce == "compass":
                        scienceDifference = techVictoryPoints(players[i].science.count("cog"), players[i].science.count("tablet"), players[i].science.count("compass")+1, players[i].effects.count("science")) - techVictoryPoints(players[i].science.count("cog"), players[i].science.count("tablet"), players[i].science.count("compass"), players[i].effects.count("science"))
                    heuristicEval.append(scienceDifference - (cardCost*goldValue))
            
            elif j.colour == "green" and players[i].ai.scienceFocus == 0:
                heuristicEval.append(2)
            
            elif j.colour == "green" and players[i].ai.scienceFocus == 1:
                heuristicEval.append(100)
                    
            elif j.colour == "brown" or j.colour == "grey":
                resourceBonus = 2
                
                if len(j.produce[0]) == 2:
                    resourceBonus += 1
                    if [j.produce[0][0]] not in players[i-1].resources:
                        resourceBonus += 0.5
                    if [j.produce[0][1]] not in players[i-1].resources:
                        resourceBonus += 0.5
                    if [j.produce[0][0]] not in players[i-2].resources:
                        resourceBonus += 0.5
                    if [j.produce[0][1]] not in players[i-2].resources:
                        resourceBonus += 0.5
                    if [j.produce[0][0]] not in players[i].resources:
                        resourceBonus += 1
                    else:
                        resourceBonus -= 0.5
                    if [j.produce[0][0]] in players[i].wonder.stage1.cost or [j.produce[0][0]] in players[i].wonder.stage2.cost or [j.produce[0][0]] in players[i].wonder.stage3.cost:
                        resourceBonus += 0.5
                    if [j.produce[0][1]] in players[i].wonder.stage1.cost or [j.produce[0][1]] in players[i].wonder.stage2.cost or [j.produce[0][1]] in players[i].wonder.stage3.cost:
                        resourceBonus += 0.5
                    if [j.produce[0][1]] not in players[i].resources:
                        resourceBonus += 1
                    else:
                        resourceBonus -= 0.5
                elif len(j.produce) == 2:
                    if j.produce[0] not in players[i-1].resources:
                        resourceBonus += 1
                    if j.produce[0] not in players[i-2].resources:
                        resourceBonus += 1
                    if j.produce[0] not in players[i].resources:
                        resourceBonus += 1
                    else:
                        resourceBonus -= 0.5
                    if [j.produce[0]] in players[i].wonder.stage1.cost or [j.produce[0]] in players[i].wonder.stage2.cost or [j.produce[0]] in players[i].wonder.stage3.cost:
                        resourceBonus += 0.5
                else:
                    if j.produce[0] not in players[i-1].resources:
                        resourceBonus += 0.5
                    if j.produce[0] not in players[i-2].resources:
                        resourceBonus += 0.5
                    if j.produce[0] not in players[i].resources:
                        resourceBonus += 1
                    else:
                        resourceBonus -= 1
                    if [j.produce[0]] in players[i].wonder.stage1.cost or [j.produce[0]] in players[i].wonder.stage2.cost or [j.produce[0]] in players[i].wonder.stage3.cost:
                        resourceBonus += 1
                
                heuristicEval.append(resourceBonus - (cardCost*goldValue))
            
            elif j.colour == "yellow":
                if j.name == "West Trading Post":
                    goldBonus = 3*goldValue
                    goldBonus += 2*goldValue * players[i-1].effects.count("brown")
                    if players[i-1].wonder.resource == ["ore"] or players[i-1].wonder.resource == ["wood"] or players[i-1].wonder.resource == ["clay"] or players[i-1].wonder.resource == ["stone"]:
                        goldBonus += 2*goldValue
                elif j.name == "East Trading Post":
                    goldBonus = 3*goldValue
                    goldBonus += 2*goldValue * players[i-2].effects.count("brown")
                    if players[i-2].wonder.resource == ["ore"] or players[i-2].wonder.resource == ["wood"] or players[i-2].wonder.resource == ["clay"] or players[i-2].wonder.resource == ["stone"]:
                        goldBonus += 2*goldValue
                elif j.name == "Tavern":
                    goldBonus = 5*goldValue
                elif j.name == "Forum":
                    goldBonus = 4
                    for x in players[i].buildings:
                        if x.colour == "grey":
                            goldBonus -= 1
                        elif x.name == "Marketplace":
                            goldBonus -= 2
                elif j.name == "Caravansery":
                    goldBonus = 7
                    for x in players[i].buildings:
                        if x.colour == "brown":
                            goldBonus -= 1
                elif j.name == "Marketplace":
                    goldBonus = 3*goldValue
                    goldBonus += (2*goldValue) * (players[i-1].effects.count("grey")+players[i-2].effects.count("grey"))
                    if players[i-1].wonder.resource == ["loom"] or players[i-1].wonder.resource == ["glass"] or players[i-1].wonder.resource == ["papyrus"]:
                        goldBonus += 2*goldValue
                    if players[i-2].wonder.resource == ["loom"] or players[i-2].wonder.resource == ["glass"] or players[i-2].wonder.resource == ["papyrus"]:
                        goldBonus += 2*goldValue
                elif j.name == "Vineyard":
                    goldBonus = (players[i].effects.count("brown") + players[i-1].effects.count("brown") + players[i-2].effects.count("brown")) * goldValue
                elif j.name == "Haven":
                    goldBonus = (players[i].effects.count("brown"))*(1+0.3333)
                elif j.name == "Lighthouse":
                    goldBonus = (players[i].effects.count("yellow"))*(1+0.3333)
                elif j.name  == "Arena":
                    goldBonus = (players[i].effects.count("wonder"))*((3*0.33333) + 1)
                heuristicEval.append(goldBonus - (cardCost * goldValue))
            
            elif j.colour == "purple":
                guildBonus = 0
                if j == spiesGuild:
                    guildBonus += players[i-1].effects.count("red") + players[i-2].effects.count("red")
                if j == magistratesGuild:
                    guildBonus += players[i-1].effects.count("blue") + players[i-2].effects.count("blue")
                if j == workersGuild:
                    guildBonus += players[i-1].effects.count("brown") + players[i-2].effects.count("brown")
                if j == craftsmensGuild:
                    guildBonus += (players[i-1].effects.count("grey") + players[i-2].effects.count("grey")) * 2
                if j == tradersGuild:
                    guildBonus += players[i-1].effects.count("yellow") + players[i-2].effects.count("yellow")
                if j == philosophersGuild:
                    guildBonus += players[i-1].effects.count("green") + players[i-2].effects.count("green")
                if j == buildersGuild:
                    guildBonus += players[i-1].effects.count("wonder") + players[i-2].effects.count("wonder") + players[i].effects.count("wonder")
                if j == shipownersGuild:
                    guildBonus += players[i].effects.count("brown") + players[i].effects.count("grey") + players[i].effects.count("purple")
                if j == strategistsGuild:
                    guildBonus += players[i-1].effects.count("loss") + players[i-2].effects.count("loss")
                if j == scientistsGuild:
                    guildBonus += techVictoryPoints(players[i].science.count("cog"), players[i].science.count("tablet"), players[i].science.count("compass"), players[i].effects.count("science")+1) - techVictoryPoints(players[i].science.count("cog"), players[i].science.count("tablet"), players[i].science.count("compass"), players[i].effects.count("science"))
                    
                heuristicEval.append(guildBonus - (cardCost * goldValue))
            
            elif j.colour == "wonder":
                wonderBonus = 0
                if type(j.produce) == int:
                    wonderBonus = j.produce
                    if age == 1:
                        wonderBonus += 2
                else:
                    if players[i].wonder == halikarnassosA:
                        if len(discardPile) == 0:
                            wonderBonus = -1
                        else:
                            wonderBonus = 4 + age
                    if players[i].wonder == rhodosA:
                        wonderBonus = 6 #Maybe FIX
                    if players[i].wonder == alexandriaA:
                        wonderBonus = 7
                        for x in players[i].buildings:
                            if x.colour == "brown":
                                wonderBonus -= 0.5
                    if players[i].wonder == babylonA:
                        wonderBonus = techVictoryPoints(players[i].science.count("cog"), players[i].science.count("tablet"), players[i].science.count("compass"), players[i].effects.count("science")+1) - techVictoryPoints(players[i].science.count("cog"), players[i].science.count("tablet"), players[i].science.count("compass"), players[i].effects.count("science"))
                    if players[i].wonder == ephesosA:
                        wonderBonus = 9 * goldValue
                    if players[i].wonder == olympiaA:
                        wonderBonus = 6 - age
                heuristicEval.append(wonderBonus - (cardCost * goldValue))
    return heuristicEval
                
def testHeuristics(games):
    vpTotal = [0,0,0]
    winCount = [0,0,0]
    allVP = []
    for gameCounter in range(games):
        vpPlus = playGame()
        for i in range(3):
            vpTotal[i] += vpPlus[3][i]
        allVP.append(vpPlus[3])
        winCount[vpPlus[3].index(max(vpPlus[3][0],vpPlus[3][1],vpPlus[3][2]))] += 1
    print("-------------------------------------------------------------")
    print("Final Results")
    print()
    for i in range(3):
        print(vpPlus[i] + " scored on average after " + str(games) + " games " + str(vpTotal[i]/games) + " points and won " + str(winCount[i]) + " of those games.")


testHeuristics(500)




