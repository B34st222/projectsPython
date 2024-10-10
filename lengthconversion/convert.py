import tkinter as tk
from tkinter import ttk 

#window
window = tk.Tk()
window.title('Demo')
window.geometry("300x600")

#title
title_label=ttk.Label(master = window, text = 'Miles to kilometer')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master=input_frame, text = "Convert")
entry.pack()
button.pack()
input_frame.pack()

#run
window.mainloop()