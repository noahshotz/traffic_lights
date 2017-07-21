### multi-threaded traffic lights
### max heinrich
### 19-07-2017
###

from threading import Timer
from Tkinter import *
import sys
import os

from Tkinter import *
from PIL import Image
from PIL import ImageTk

'''gui'''

root = Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(400, 400))

image = Image.open('bg.jpg')
photo_image = ImageTk.PhotoImage(image)
label = Label(root, image = photo_image)
label.pack()

light1 = (["red", "yellow", "green"])
light2 = (["red", "yellow", "green"])
light3 = (["red", "yellow", "green"])
light4 = (["red", "yellow", "green"])

### go - 0
### pending - 1
### stop - 2

### state1 vertical go - horizontal stop 
### light1 array index 2
### light2 array index 2
### light3 array index 0
### light4 array index 0

### state1 vertical go - horizontal stop
### state2 vertical pending - horizontal stop
### state3 vertical stop - horizontal pending
### state4 vertical stop - horizontal go
### state5 vertical stop - horizontal pending
### state6 vertical pending - horizontal stop

def state1():
	print "###"
	#vertical
	state1light1 = light1[2] #go
	print state1light1
	state1light2 = light2[2] #go
	print state1light2
	#horizontal
	state1light3 = light3[0] #stop
	print state1light3
	state1light4 = light4[0] #stop
	print state1light4
	print "###"

	light1 = Label(root, background = "red")
	light1.place(x = 118, y = 118, width = 20, height = 20)

def state2():
	clearTerminal()
	print "###"
	#vertical
	state2light1 = light1[1] #pending
	print state2light1
	state2light2 = light2[1] #pending
	print state2light2
	#horizontal
	state2light3 = light3[0] #stop
	print state2light3
	state2light4 = light4[0] #stop
	print state2light4
	print "###"


def state3():
	clearTerminal()
	print "###"
	#vertical
	state3light1 = light1[0] #stop
	print state3light1
	state3light2 = light2[0] #stop
	print state3light2
	#horizontal
	state3light3 = light3[0] #pending
	print state3light3
	state3light4 = light4[0] #pending
	print state3light4
	print "###"

def state4():
	clearTerminal()
	print "###"
	#vertical
	state4light1 = light1[0] #stop
	print state4light1
	state4light2 = light2[0] #stop
	print state4light1
	#horizontal
	state4light3 = light3[0] #go
	print state4light1
	state4light4 = light4[0] #go
	print state4light1
	print "###"

def state5():
	clearTerminal()
	print "###"
	#vertical
	state4light1 = light1[0] #stop
	print state4light1
	state4light2 = light2[0] #stop
	print state4light1
	#horizontal
	state4light3 = light3[0] #go
	print state4light1
	state4light4 = light4[0] #go
	print state4light1
	print "###"

def state6():
	clearTerminal()
	print "###"
	#vertical
	state4light1 = light1[0] #stop
	print state4light1
	state4light2 = light2[0] #stop
	print state4light1
	#horizontal
	state4light3 = light3[0] #pending
	print state4light1
	state4light4 = light4[0] #pending
	print state4light1
	print "###"

def state7():
	clearTerminal()
	print "###"
	#vertical
	state4light1 = light1[0] #pending
	print state4light1
	state4light2 = light2[0] #pending
	print state4light1
	#horizontal
	state4light3 = light3[0] #stop
	print state4light1
	state4light4 = light4[0] #stop
	print state4light1
	print "###"

def clearTerminal():
	os.system("clear") #clear terminal after each state output

t1 = Timer(1.0, state1)
t2 = Timer(6.0, state2)
t3 = Timer(11.0, state3)
t4 = Timer(16.0, state4)
t5 = Timer(21.0, state5)
t6 = Timer(26.0, state6)
t7 = Timer(31.0, state7)

def switch():
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()
	t6.start()
	t7.start()

user_input = input()
if user_input == 0:
	switch()

root.mainloop()


