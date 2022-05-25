"""
Intro 

    MYSTOS presentation in python 3rd and Final revision 5/24/22 by Joseph Sylvester- Thank you for viewing, the following is a fun project I designed
 on my own time to be a presentation of my knowledge of the many key features of the python inerpreted programming language, I have commented each function
 to better describe what they do and also have named the variables to make it easier to discern their meaning.
 The benifits of using python in business often outweigh that of it's flaws, so I feel this is a valuable skill to display. In this revision, given more time,
 I've refactored my code to run more efficiently. I hope you enjoy, thank you for viewing.

"""
from time import sleep # I need more sleep, I don't get enough.
from mystosxdata import *
import mystosxgui
import mystosxchars #Needed for character dictionary get and set

characteristics = mystosxchars.playercharacter # variable for new instance of the playercharacter class
enemyNPC=mystosxchars.proceduralEnemy  # variable for new instance of the enemy class
#The collapsed function will handle player login 
def login():
    classNames= [["Wayra","Viridi","Kamil","Bon"]["white","green","red","blue"]["Soldier", "Rogue","Scholar"]]
     #list of lists

    print("What is your name traveller?")
    playername = input()
    characteristics.characterstats_dictionary["playername"] = playername
    print("What is your password?")
    password = input()
    
    characteristics.characterstats_dictionary["password"] = password
    characteristics.characterstats_dictionary=loadsaveGame(characteristics.characterstats_dictionary)
    
    #Player class choice
    if characteristics.characterstats_dictionary["playerclass"]=="": class_chosen = 0
    else: class_chosen = 1
    while class_chosen == 0:
        print("Will you choose the path of the soldier, thief or scholar?")
        playerclass = str.upper(input())
        if playerclass == "SOLDIER":
            class_chosen = 1
            characteristics.characterstats_dictionary["playerclass"]= playerclass
            print ("You have chosen the path of the " + characteristics.characterstats_dictionary["playerclass"])
            
        elif playerclass == "THIEF":
            class_chosen = 1
            characteristics.characterstats_dictionary["playerclass"]= playerclass
            print ("You have chosen the path of the " + characteristics.characterstats_dictionary["playerclass"])
        elif playerclass == "SCHOLAR":
            characteristics.characterstats_dictionary[["playerclass"]]= playerclass
            class_chosen = 1
            print ("You have chosen the path of the " + characteristics.characterstats_dictionary["playerclass"])
        else:
            print("That is not a valid entry...")
            class_chosen = 0
    
    #Player Diety choice        
    if characteristics.characterstats_dictionary["diety"]== "" : 
        complete=0
        while complete == 0:
            print ("Go to the green, red, blue or white light? You won't be able to turn back.")
            startcolor_choice = str.upper(input())
            if startcolor_choice == "GREEN": # setting and getting values via dictionary 
                characteristics.characterstats_dictionary ["diety"]= "Viridi"
                print(characteristics.characterstats_dictionary["diety"] + "|" + " Hello " + characteristics.characterstats_dictionary["playerclass"] + " we have been waiting for you. I knew you would choose me.")
                complete = 1
                print (characteristics.characterstats_dictionary["diety"] + "|" + " My name is " + characteristics.characterstats_dictionary["diety"] + ".")
            elif startcolor_choice == "RED":
                characteristics.characterstats_dictionary ["diety"] = "Kamil"
                print(characteristics.characterstats_dictionary["diety"] + "|" + " Hello " + characteristics.characterstats_dictionary["playerclass"] + " we have been waiting for you. I knew you would choose me.")
                complete = 1
                print (characteristics.characterstats_dictionary["diety"] + "|" + " My name is " + characteristics.characterstats_dictionary["diety"] + ".")
            elif startcolor_choice == "BLUE":
                characteristics.characterstats_dictionary ["diety"] = "Bonz"
                print(characteristics.characterstats_dictionary["diety"] + "|" + " Hello " + characteristics.characterstats_dictionary["playerclass"] + " we have been waiting for you. I knew you would choose me.")
                complete = 1
                print (characteristics.characterstats_dictionary["diety"] + "|" + " My name is " + characteristics.characterstats_dictionary["diety"] + ".")
            elif startcolor_choice == "WHITE":
                characteristics.characterstats_dictionary ["diety"] = "Wayra"
                print(characteristics.characterstats_dictionary["diety"] + "|" + " Hello " + characteristics.characterstats_dictionary["playerclass"] + " we have been waiting for you. I knew you would choose me.")
                complete = 1
                print (characteristics.characterstats_dictionary["diety"] + "|" + " My name is " + characteristics.characterstats_dictionary["diety"] + ".")
            else:
                input ("That is not a valid entry...")

    
# main 
 
login()
input("Press any key to continue...")
sleep(3)
print(" You gain 600 experience ")
sleep(2)
print("You encounter a creature")
characteristics.addStats("experience", 600)
loadsaveGame(characteristics.characterstats_dictionary)
print(characteristics.characterstats_dictionary["diety"])
mystosxgui.runGUI(characteristics.getStats(),enemyNPC.newEnemy(characteristics.characterstats_dictionary["level"]))








