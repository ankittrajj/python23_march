# import tkinter module
from tkinter import *

# make a object of tkinter.
window = Tk()
window.title("my first app")

# create a function for submit button
def click():
    enter_text = str(textbox.get())
    output.delete(0.0,END)

#     exceptional handling
    try:
        define = my_dict[enter_text]
    except:
        define = 'not available in the database'
    output.insert(END,define)





#
# Label(window,text='Enter your name',bg='red',fg='black',font='aerial 16 bold').grid(row=0,column=0,sticky=W)
#
textbox = Entry(window,width = 50,bg='white',fg='black').grid(row = 0,column=1,sticky=W)
#
# # button
# Button(window,text = 'SUBMIT',bg = 'gray',fg='black',font = 'aerial 20 bold').grid(row=1,column=2,sticky=W)



# mini project
# create a label
Label(window,text = 'Define the data',bg='yellow',fg='black',font='aerial 20 bold').grid(row=0,column=0,sticky=W)

# create a output box
output = Text(window,width=20,height=5,bg='white',font='aerial 12 bold')
output.grid(row=0,column=2,sticky=W)

# button
Button(window,text = 'SUBMIT',command = click,bg = 'gray',fg='black',font = 'aerial 20 bold').grid(row=1,column=2,sticky=W)


# make a data
my_dict = {
    'animal': 'dog',
    'bird':'parrot'
}



# run the app for infinite times.
window.mainloop()





