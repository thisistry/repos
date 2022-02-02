import tkinter as tk 
from tkinter import *

win = Tk() 

#to specify size of window. 
win.geometry("250x170") 

# To Create a text widget and specify size. 
T = Text(win, height = 6, width = 53) 

# TO Create label 
l = Label(win, text = "Quote for the Day") 
l.config(font =("Courier", 14)) 

Quote = """Success usually comes to those who are too busy to be looking for it"""

# Create a button for the next text. 
b1 = Button(win, text = "Next", ) 

# Create an Exit button. 
b2 = Button(win, text = "Exit", 
			command = win.destroy) 

l.pack() 
T.pack() 
b1.pack() 
b2.pack() 

# Insert the Quote 
T.insert(tk.END, Quote) 

tk.mainloop() 

CT-2354 : [TS.31.121][SIM_CT][ND_Testing][CATNB][FAIL][TC.7.1.4][FPLMN expected and received record mismatch], CT-2354, CT-2362 : [TS.31.121][SIM_CT][ND_Testing][CATNB][FAIL][TC.7.1.4][FPLMN expected and received record mismatch], [TS.36.523][CAT-NB ASIC A0][FAIL][TC.22.5.1][Authentication failure message is not triggered with the EMM cause 21]

Source      : Alif Semiconductor
JIRA ID     : CT-2354, CT-2362
REVIEW ID   : 3417
Type        : Defect Fix
Disposition : Local
Description : [TS.31.121][SIM_CT][ND_Testing][CATNB][FAIL][TC.7.1.4][FPLMN expected and received record mismatch], [TS.36.523][CAT-NB ASIC A0][FAIL][TC.22.5.1][Authentication failure message is not triggered with the EMM cause 21]

Reviewed-by : Jagdeep,Dushyantha
