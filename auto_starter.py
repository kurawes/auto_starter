import tkinter as tk
import os
from tkinter import filedialog, Text


# main anchor element
root = tk.Tk()


# creates the program window
canvas = tk.Canvas(root, height=700, width=700, bg="light blue")
canvas.pack()   # attaches canvas to the root


# Runs the main loop
root.mainloop()