import random
import json
class playercharacter():
    
    
    characterstats_dictionary = { 
        "level" : 1,
        "experience":0.00,
        "exptolvl":501.00,
        "strength" : 5.0,
        "dexterity" : 5.0,
        "intellegence" : 5.0,
        "spirit" : 5.0,
        "constitution" : 5.0, 
        "vitality" : 5.0,

        "health": 0.0,
        "mana": 0.0,
        "armor" : 0.0, 
        "dodge": 0.0, 
        "accuracy" : 0.0, 
        "spellaccuracy" : 0.0, 
        "critchance" : 0.0, 
        "critmulti" : 0.0, 
        "affinity" : 0.0, 
        "diety" : "",
        "favor" : 0.0, 
        "playerclass" : "",
        "playername" : "",
        "password": "",
        "locationX" : 0.0 ,
        "locationY" : 0.0,
        }
    
    def getStats():
    
        return playercharacter.characterstats_dictionary
    
    def addLevel():
        playercharacter.characterstats_dictionary["level"]+=1
        playercharacter.characterstats_dictionary["exptolvl"]*=2
    
        if playercharacter.characterstats_dictionary["playerclass"] == "SOLDIER":
            playercharacter.addStats("strength", 5)
            playercharacter.addStats("dexterity", 3)
            playercharacter.addStats("intellegence", 1)
            playercharacter.addStats("spirit", 1)
            playercharacter.addStats("constitution", 4)
            playercharacter.addStats("vitality", 4)
    
        elif playercharacter.characterstats_dictionary["playerclass"] == "THIEF":
            playercharacter.addStats("strength", 2)
            playercharacter.addStats("dexterity", 5)
            playercharacter.addStats("intellegence", 3)
            playercharacter.addStats("spirit", 2)
            playercharacter.addStats("constitution", 3)
            playercharacter.addStats("vitality", 3)   
    
        elif playercharacter.characterstats_dictionary["playerclass"] == "SCHOLAR":
            playercharacter.addStats("strength", 1)
            playercharacter.addStats("dexterity", 2)
            playercharacter.addStats("intellegence", 5)
            playercharacter.addStats("spirit", 4)
            playercharacter.addStats("constitution", 2)
            playercharacter.addStats("vitality", 3)
    
        else: 
            print ("error")
        playercharacter.characterstats_dictionary["health"]= 100 + (playercharacter.characterstats_dictionary["vitality"]*5)
        playercharacter.characterstats_dictionary["mana"]=100 + (playercharacter.characterstats_dictionary["intellegence"]*5) 


    def changeLocation(x,y):
        playercharacter.characterstats_dictionary["locationX"]+=x
        playercharacter.characterstats_dictionary["locationY"]+=y
    
    def calcStats():
        playercharacter.characterstats_dictionary["armor"]= 100 + (playercharacter.characterstats_dictionary["constitution"]*5)
        playercharacter.characterstats_dictionary["dodge"]=100 + (playercharacter.characterstats_dictionary["dexterity"]*5)
        playercharacter.characterstats_dictionary["accuracy"]= 100 + (playercharacter.characterstats_dictionary["dexterity"]*5)
        playercharacter.characterstats_dictionary["spellaccuracy"]= 100 + (playercharacter.characterstats_dictionary["spirit"]*5)
        playercharacter.characterstats_dictionary["critchance"]= 100 + (playercharacter.characterstats_dictionary["dexterity"]*3)
        playercharacter.characterstats_dictionary["critmulti"]= 100 + (playercharacter.characterstats_dictionary["strength"]*3)
        playercharacter.characterstats_dictionary["favor"]= 100 + (playercharacter.characterstats_dictionary["spirit"]*5)
        



    def addStats(trgtField,newValue):
        playercharacter.characterstats_dictionary[trgtField]+=newValue
        if playercharacter.characterstats_dictionary["experience"] >= playercharacter.characterstats_dictionary["exptolvl"]:
            playercharacter.addLevel()
            playercharacter.calcStats()
        else:
            playercharacter.calcStats()



class proceduralEnemy:
    enemyNames= ["Goblin", "Skeleton", "Blob","Zombie"]
    enemyPrefix=["Lazy","Rude","Strong","Fire", "Ice", "Poison", "Elder"]
    enemySuffix=["Speed","Ironskin","Wrath","the End"]

    def newEnemy(character_lvl):
        def concatName(pprefix = "", nname = "", ssuffix = ""):
            if len(pprefix)>1:
                return pprefix + " " + nname
            elif len(pprefix) > 1 and len(ssuffix) > 1:
                return pprefix + " " +  nname  + " of " + ssuffix
            else:
                return nname
        def enemyStats(enemy_lvl=character_lvl, enemy_prefix=0, enemy_name=0, enemy_suffix=0, enemyFinal=""):
            
            newEnemy_dictionary={
                "enemyname":enemyFinal,
                "health" : (enemy_lvl*10)+((enemy_prefix+enemy_suffix)*enemy_name+1),
                "damage": (enemy_prefix+enemy_suffix)*enemy_name,
                "mana": (enemy_lvl*10)+((enemy_prefix+enemy_suffix)*enemy_name+1),
                "armor" : (enemy_prefix+enemy_suffix)*enemy_name+1, 
                "dodge": (enemy_prefix+enemy_suffix)*enemy_name+1, 
                "accuracy" : (enemy_prefix+enemy_suffix)*enemy_name+1, 
                "spellaccuracy" : (enemy_prefix+enemy_suffix)*enemy_name+1, 
                "critchance" : (enemy_prefix+enemy_suffix)*enemy_name+1, 
                "critmulti" : (enemy_prefix+enemy_suffix)*enemy_name+1,
            }
            return newEnemy_dictionary

        if character_lvl <= 1:
            enemy=""
            _y=random.randint(0,len(proceduralEnemy.enemyNames)-1)
            enemy=proceduralEnemy.enemyNames[_y]
            return enemyStats(character_lvl,0,_y,0,enemy)
        elif character_lvl > 2 and character_lvl < 4:
            enemy=""
            _x=random.randint(0,len(proceduralEnemy.enemyPrefix)-1)
            _y=random.randint(0,len(proceduralEnemy.enemyNames)-1)
            enemy= concatName(proceduralEnemy.enemyPrefix[_x],proceduralEnemy.enemyNames[_y],"")
            return enemyStats(character_lvl,_x,_y,0,enemy)
        else:
            enemy=""
            _x=random.randint(0,len(proceduralEnemy.enemyPrefix)-1)
            _y=random.randint(0,len(proceduralEnemy.enemyNames)-1)
            _z=random.randint(0,len(proceduralEnemy.enemySuffix)-1)
            enemy= concatName(proceduralEnemy.enemyPrefix[_x],proceduralEnemy.enemyNames[_y], proceduralEnemy.enemySuffix[_z])
            return enemyStats(character_lvl,_x,_y,_z,enemy)

    





            








    


