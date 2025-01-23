from tkinter import *

langas = Tk()

langas.geometry("250x250")
virsutinis = Frame(langas)
apatinis = Frame(langas)

mygtukas1 = Button(virsutinis, text="1 mytukas")
mygtukas2 = Button(virsutinis, text="2 mytukas")
mygtukas3 = Button(virsutinis, text="3 mytukas")
mygtukas4 = Button(apatinis, text="4 mytukas")

virsutinis.pack()
apatinis.pack(side=RIGHT)
mygtukas1.pack(side=LEFT)
mygtukas2.pack(side=RIGHT)
mygtukas3.pack(side=RIGHT)
mygtukas4.pack(side=BOTTOM, fill=X)

langas.mainloop()
