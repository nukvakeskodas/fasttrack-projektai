from tkinter import *
langas = Tk()

#def spausdinti():
#   ivesta = laukas1.get()
#    rezultatas['text'] = ivesta

kintamasis = StringVar(" ")
#kintamasis = ""

def funkcija():
    kintamasis.set("Naujas tekstas")
    print(kintamasis.get())   
    
uzrasas1 = Label(langas, text='Įrašykite žodį')
#laukas1 = Entry(langas)
mygtukas = Button(langas, text='Įvesti', command = funkcija)
rezultatas = Label(langas, text="")

uzrasas1.grid(row=0,column=0)
#laukas1.grid(row=0,column=1)
mygtukas.grid(row=0,column=2)
rezultatas.grid(row=1,columnspan=3)


langas.mainloop()