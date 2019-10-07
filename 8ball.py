import time
from random import randint
from tkinter import *
import sys

def random():
	choices=[str(x)+" ways do this this" for x in range(0,20)]
	
	x=randint(2,19)
	
	return(choices[x])
def window():
	window = Tk()
	window.title("Magic 20 Ball")
	lbl=Label(window, text="Hello! Do you want to ask a question? Y/N")
	lbl.grid(column=1,row=0)
	window.geometry('800x600')
	btn=Button(window, text="Tell me, Magic 20 Ball!", command=clicked)
	btn.grid(column=0,row=1)
	txt=Entry(window, width=20)
	txt.grid(column=0,row=2)
	txt.focus()
	window.mainloop()
	
def clicked():
	if (txt.get()=="Y"):
		lbl.configure(text="Thinking...")
		lbl.update()
		time.sleep(2)
		clicked2()
	elif (txt.get()=="N"):
		sys.exit(0)
	else:
		lbl.configure(text="Wrong input")
		clicked()

		
def clicked2():
	lbl.configure(text="Thinking still...")
	lbl.update()
	time.sleep(2)

	lbl.configure(text=random())
	lbl.update()
	time.sleep(2)
	reset()

def reset():
	lbl.configure(text="Hello! Do you want to ask a question? Y/N")

def main():
	response=""
	while (response==""):
		
		response=input("Hello! Do you want to ask a question? Y/N\n")
		
		if (response=="Y" or response=="y"):
			temp=input("What do you want to ask?\n")
			response=""
			random()				
		elif (response!="n" and response!="N"):
			print ("Error: Incorrect input. Please type Y or N.")
			response=""
			
window = Tk()
window.title("Magic 20 Ball")
lbl=Label(window, text="Hello! Do you want to ask a question? Y/N")
lbl.grid(column=1,row=0)
window.geometry('800x600')
btn=Button(window, text="Tell me, Magic 20 Ball!", command=clicked)
btn.grid(column=0,row=1)
txt=Entry(window, width=20)
txt.grid(column=0,row=2)
txt.focus()
window.mainloop()
main()
	