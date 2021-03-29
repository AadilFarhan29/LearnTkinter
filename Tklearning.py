from tkinter import *

root = Tk() # This is important for All Tk inter project 

def myClick(): # You can add a command/function for your buttons. like this . 
    mylabel = Label(root, text= "Hey look i clicked a button ! ! ! ").grid(row= 1 , column= 0) 
    

#mylabel = Label(root, text = "Hello World! ").grid(row = 0 , column= 0) #Creating a Label
#mylabel2 = Label(root, text = "My name is Aadil Farhan.").grid(row = 1 , column= 0)

#Creating a button.
mybutton = Button(root, text = "Click Me ! " , padx= 30, command= myClick, fg= "white", bg= "black").grid(row = 0 , column= 0) # we can disable a button by giving state = DISABLE we can change the size of the button using padx and pady.we can also change the color using fg and bg


#mylabel.pack() # Shoving my data is onto the screen (this one keeps the text in the middle.)

'''

mylabel.grid(row = 0 , column= 0)
mylabel2.grid(row = 1, column= 0) # We can Assign where the text should be displayed. 
instead of doing this we can also  also paste the grid into label. the actual label 
which gives the same result. For cleaner code we can use this. 

'''

root.mainloop() #It is reauied to create a GUI (graphical user interface)
