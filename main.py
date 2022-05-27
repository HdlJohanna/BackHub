import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox 
import utils
import time

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = srcdir.get()
	return userInput



def prog():
    window = Tk()
    percent = StringVar()
    text = StringVar()

    bar = ttk.Progressbar(window,orient=HORIZONTAL,length=utils.getDiskSpace(srcdir.get()))
    bar.pack(pady=10)

    PercentLabel = Label(window,textvariable=percent).pack()
    taskLabel = Label(window,textvariable=text).pack()
    GB = utils.getDiskSpace()
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" Byte completed")
        window.update_idletasks()

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = destdir.get()
	return userInput


"""# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValue():
	checkedOrNot = overwrite.get()
	return checkedOrNot"""


# this is the function called when the button is clicked
def backupStart():
    print("Starting Backup...")
    res = utils.backup(srcdir.get(),destdir.get())
    if isinstance(res, int):
        messagebox.showinfo("BackHub", f"Backup completed successfully\n{res} files copied")
    else:
        messagebox.showerror("BackHub", f"Backup failed: \n{res}")



root = Tk()
#this is the declaration of the variable associated with the checkbox
overwrite = tk.IntVar()



# This is the section of code which creates the main window
root.geometry('436x212')
root.configure(background='#F0F8FF')
root.title('BackHub')


# This is the section of code which creates the a label
Label(root, text='Source Directory:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=24, y=17)


# This is the section of code which creates the a label
Label(root, text='Destination Directory', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=26, y=40)


# This is the section of code which creates a text input box
srcdir=Entry(root)
srcdir.place(x=191, y=18)


# This is the section of code which creates a text input box
destdir=Entry(root)
destdir.place(x=192, y=42)


# This is the section of code which creates a button
Button(root, text='Back Up', bg='#F0F8FF', font=('arial', 12, 'normal'), command=backupStart).place(x=265, y=71)


root.mainloop()
