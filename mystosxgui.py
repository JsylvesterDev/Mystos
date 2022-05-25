import tkinter



def runGUI(playerDict,npcDict):

    guiWindow= tkinter.Tk()
    
    termDisp= tkinter.Text()

    guiWindow.title("Mystos")
    guiWindow.minsize(800,450)

    charstatDisp = tkinter.Label(guiWindow,text=playerDict).grid(row=1,column=0,rowspan=4,columnspan=1)
    spaceMid= tkinter.Label(guiWindow,text="         ").grid(row=1,column=1,rowspan=2,columnspan=3)
    spaceTop= tkinter.Label(guiWindow,text="      ").grid(row=0,column=0,rowspan=1,columnspan=5)
    npcDisp= tkinter.Label(guiWindow,text=npcDict).grid(row=1,column=5,rowspan=4,columnspan=1)
    






    
    guiWindow.mainloop()
