from tkinter import *

root = Tk() # This is important for All Tk inter project 
root.title("Basic of Tkinter.") #For adding title 



entry = Entry(root, width= 50,fg= "white", bg= "black", borderwidth= 5)#.grid(row= 0 , column=2) # we can add a input box using this command.
entry.pack()
entry.insert(0, "Enter your name here: ")

def myClick(): # You can add a command/function for your buttons. like this . 
    b = "Hello " + entry.get()
    mylabel = Label(root, text= b)#.grid(row= 1 , column= 5) 
    mylabel.pack()

#mylabel = Label(root, text = "Hello World! ").grid(row = 0 , column= 0) #Creating a Label
#mylabel2 = Label(root, text = "My name is Aadil Farhan.").grid(row = 1 , column= 0)

#Creating a button.
mybutton = Button(root, text = "Enter Your Name  " , padx= 30, command= myClick, fg= "white", bg= "black")#.grid(row = 0, column= 10) # we can disable a button by giving state = DISABLE we can change the size of the button using padx and pady.we can also change the color using fg and bg
mybutton.pack()

#mylabel.pack() # Shoving my data is onto the screen (this one keeps the text in the middle.)

'''

mylabel.grid(row = 0 , column= 0)
mylabel2.grid(row = 1, column= 0) # We can Assign where the text should be displayed. 
instead of doing this we can also  also paste the grid into label. the actual label 
which gives the same result. For cleaner code we can use this. 

'''

root.mainloop() #It is reauied to create a GUI (graphical user interface)
