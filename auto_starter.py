import tkinter as tk
import os
from tkinter import Grid, filedialog, Text


# main anchor element
root = tk.Tk()

apps = []   # a list for apps added 

if os.path.isfile("savedapps.txt"):
    with open("savedapps.txt", "r") as f:
        tempApps = f.read()
        appsTemp = tempApps.split(",")  #split the file at every comma
        apps = [x for x in appsTemp if x.strip()]   # remove empty spaces in the list



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


def runApps():
    for app in apps:
        os.startfile(app)   # loops over the list and runs the apps


def clearAllExecutables():
    apps.clear()    # clears the app list
    for app in frame.winfo_children():   # loop through items in the frame
        app.destroy()    # delete previously added apps
    

# create the program window
canvas = tk.Canvas(root, height=700, width=700, bg="light blue")
canvas.pack(fill="both", expand = True)   # attach canvas to the root, fill the canvas even when rezising


#create frame inside the main window
frame = tk.Frame(root, bg="gray")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

frame2 = tk.Frame(root, bg="gray")
frame2.place(relheight=0.05, relwidth=0.8, relx=0.1, rely=0.9)


#add buttons to the root window
openFile = tk.Button(frame2, text="Open App", fg="black", bg="light blue", command=addApp)
openFile.grid(row=0, column=0) # attach open file button to the frame

runallApps = tk.Button(frame2, text="Run Apps",fg="black", bg="light blue", command=runApps)
runallApps.grid(row=0, column=1)

removeApp = tk.Button(frame2, text="Remove App", fg="black", bg="light blue")
removeApp.grid(row=0, column=2)

clearAllApps = tk.Button(frame2, text="Clear all", fg="black", bg="light blue", command=clearAllExecutables)
clearAllApps.grid(row=0, column=3)

# Configure the columns and rows for the buttons
frame2.grid_columnconfigure((0,1,2,3), weight=1)
frame2.grid_rowconfigure(0, weight=1)


# add the programs from the save file to the frame
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


# Run the main loop
root.mainloop()

# save the selected apps to a file
with open("savedapps.txt", "w") as f:
    for app in apps:
        f.write(app + ",")