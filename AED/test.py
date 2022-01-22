from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x500")
window.title("Test")

lbox_comentarios = Listbox(window,height=7, width=65, selectmode="single")
lbox_comentarios.place(x=20, y=20)

nome_selecao = "Nome do filme"

comentarios = open("comentarios.txt", "r")
all_comments = comentarios.readlines()
for line in all_comments:
    campo = line.split(";")
    if nome_selecao not in campo:
        lbox_comentarios.insert(END,"Ainda não existem comentários!")
    elif campo[0] == nome_selecao:
        for i in range(len(campo)-1,0,-1):
            lbox_comentarios.insert(END,campo[i])
storage = open("storage.txt", "a")
comentarios.write(str())
comentarios.close()

window.mainloop()