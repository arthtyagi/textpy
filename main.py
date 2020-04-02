import sys
from tkinter import *
import tkinter.tkFileDialog

main=Tk("TextPy")

textorg=Text(main)
textorg.grid()

def saveas():

    global textorg

    t = textorg.get("1.0", "end-1c")

    saveloc=tkFileDialog.asksaveasfilename()

    f1=open(saveloc, "w+")

    f1.write(t)

    f1.close()

button=Button(main, text="Save as", command=saveas)
button.grid() 
main.mainloop()
