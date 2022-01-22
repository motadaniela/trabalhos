from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x500")
window.title("Test")

lbox_comentarios = Listbox(window,height=7, width=65, selectmode="single")
lbox_comentarios.place(x=20, y=20)

nome_selecao = "line"
txt_comentario = "text text text"
username = "user123"

comentarios = open("comentarios.txt", "r")
all_comments = comentarios.readlines()
for line in all_comments:
    campo = line.split(";")
    if campo[0] == nome_selecao:
        all_comments[all_comments.index(line)] = (line[0:len(line)-2]) + ";" + username + ": " + txt_comentario +"\n"  #muda o elemento da lista(linha com todos os comentarios de um determinado filme/serie)
        comentarios = open("comentarios.txt", "w")
        comentarios.write("")     #apaga todo o ficheiro
        comentarios = open("comentarios.txt", "a")
        for i in range(len(all_comments)):
            comentarios.write(all_comments[i])  #volta a colocar toda a informacao no ficheiro com a adicao do novo comentario
comentarios.close()

window.mainloop()

