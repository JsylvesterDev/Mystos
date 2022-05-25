import json

def loadsaveGame( _charStats):     
    mdb_playername=_charStats["playername"]
    mdb_playerpass=_charStats["password"]
    mdb_CharDict= {mdb_playername :_charStats}
        
    try:
        with open("mystosxcharsaves.json",'r') as character_SaveFile:

            saved_Characters = json.load(character_SaveFile)
            charInst=saved_Characters[mdb_playername]
            charInstPass=saved_Characters[mdb_playername]["password"]
            
            if mdb_playername in saved_Characters and mdb_playerpass == charInstPass:
            
                return charInst

            elif mdb_CharDict in charInst['playername'] and mdb_playerpass != charInst["password"]:

                print ("Choose another name, that one is taken")
                rerollName=input()
                loadsaveGame(rerollName,mdb_playerpass,mdb_CharDict)
            else:

                saved_Characters = json.update(mdb_CharDict)
                return saved_Characters[mdb_playername]
        
    except:

        with open("mystosxcharsaves.json",'w') as character_SaveFile:

            saved_Characters = json.dump(mdb_CharDict,character_SaveFile)
            if mdb_CharDict in saved_Characters and mdb_playerpass == saved_Characters[mdb_playername["password"]]:
            
                return saved_Characters[mdb_playername]

            elif mdb_CharDict in saved_Characters and mdb_playerpass != saved_Characters[mdb_playername["password"]]:

                print ("Choose another name, that one is taken")
                rerollName=input()
                loadsaveGame(rerollName,mdb_playerpass,mdb_CharDict)
            else:

                saved_Characters = json.update(mdb_CharDict)
                return saved_Characters[mdb_playername]
    finally:

        