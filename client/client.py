from tkinter import *
from connection import *

def change_label_text():
	global label
	label['text'] = get_label_text()

def update():
	start_server()
	change_label_text()

main_window = Tk()
main_window.title('Start server')
main_window.geometry('300x300')


buttonText = "Start server remotely"

b = Button(main_window, text = buttonText, command = update)
b.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label = Label(main_window, text = 'Click the button below.')
label.pack()

mainloop() 
