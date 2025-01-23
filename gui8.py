import tkinter as tk

def update_label(*args):
    label_text.set(entry_text.get())

root = tk.Tk()

entry_text = ""
entry_text.trace("w", update_label)

entry = tk.Entry(root, textvariable=entry_text)
entry.pack()

label_text = tk.StringVar()
label_text.set("Your Text Will Appear Here")
label = tk.Label(root, textvariable=label_text)
label.pack()

root.mainloop()
