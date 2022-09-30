import tkinter as tk
    

def write():
    print("welcome to GUI")

root = tk.Tk()
win= tk.Frame(root)
win.pack()

button = tk.Button(win, text="QUIT", fg="red",command=quit)
button.pack(side=tk.LEFT)
sen = tk.Button(win,text="Enter",command=write)
sen.pack(side=tk.LEFT)

root.mainloop()