'''
Introduction to Tkinter Windows and Widgets
    The top-level window object in GUI Programming contains all of the little window objects that will be part of your complete GUI.
    The little window objects can be text labels, buttons, list boxes, etc., and these individual little GUI components are known as Widgets.
    So, having a top-level window object will act as a container where you will put all your widgets. In Python, you'd typically do so like this using the following code: win = Tk()
    The object that is returned by making a call to Tk() is usually referred to as the Root Window.

Tkinter Button Widget
This widget can be used to make different types of buttons.
We can have buttons containing not only text, but also images!
In Python, while using the Tkinter button widget, we can easily modify the style of the button by adding a background color to it, adjusting height and width of button, or the placement of the button, etc. very easily.
Tkinter Button Widget
'''

import tkinter
win = tkinter.Tk()  # win is a top or parent window
win.geometry("400x200")

label1 = tkinter.Label(win, text = "hi, welcome to GUI using Tkinter")
label1.pack()

c = tkinter.Checkbutton(win, text = "Python") 
c.pack()  
c1 = tkinter.Checkbutton(win, text = "C++") 
c1.pack() 
c2 = tkinter.Checkbutton(win, text = "C") 
c2.pack() 

b = tkinter.Button(win, text = "Submit")    #Button Widget
b.pack()  #using pack() geometry

win.mainloop()