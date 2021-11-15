import tkinter as tk
import os
from tkinter import filedialog, Text


# main anchor element
root = tk.Tk()
apps = []

def addApp():
    for widget in frame.winfo_children():   # loop through items in the frame
        widget.destroy()    # delete previously added apps

    # open up a dialog box to add apps to the frame
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="light blue")
        label.pack()   # attach the program name to the frame

# create the program window
canvas = tk.Canvas(root, height=700, width=700, bg="light blue")
canvas.pack()   # attach canvas to the root


#create frame inside the main window
frame = tk.Frame(root, bg="gray")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)


#add buttons to the root window
openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="black", bg="light blue", command=addApp)
openFile.pack() # attach open file to the root

runApps = tk.Button(root, text="Run Apps", padx=10,
                     pady=5, fg="black", bg="light blue")
runApps.pack()


# Run the main loop
root.mainloop()