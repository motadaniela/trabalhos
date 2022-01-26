from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x500")
window.title("Test")

nome_selecao = "Nome"
#txt_comentario = "text text text"
username = "123"
spin = 6

button = Button(window,height=3, width=10, text=">", command = lambda: remove_favoritos(nome_selecao, username))
button.place(x=20, y=20)

def remove_favoritos(nome_selecao, username):
    favoritos = open("Favoritos.txt", "r", encoding="UTF-8")
    lista = favoritos.readlines()
    for line in lista:
        campos = line.split(";")
        if username == campos[0]:
            break
    for i in range(len(campos)):
        if campos[i] == nome_selecao or campos[i] == nome_selecao + "\n":
            campos[i] = ""
            new_line = ""
#ISTO E A PARTE QUE E SUPOSTO TIRAR OS DUPLOS ;
            for i in range(len(campos)):
                new_line += campos[i] +";"
            for i in range(new_line.count(";")):
                new_line.replace(";;",";")
            lista[lista.index(line)] = new_line[0:len(new_line)-2] + "\n"
            favoritos = open("Favoritos.txt", "w")
            favoritos.write("")
            favoritos = open("Favoritos.txt", "a", encoding="UTF-8")
            for i in range(len(lista)):
                favoritos.write(str(lista[i]))
            msg = messagebox.showinfo("Adicionado aos favoritos!","{0} foi removido da sua lista de favoritos!".format(nome_selecao))
            break


window.mainloop()