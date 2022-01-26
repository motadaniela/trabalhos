from cgitb import text
from distutils import command
import encodings
from optparse import Values
from tkinter import *
from tkinter import ttk
from tokenize import String
from turtle import width
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import tkinter as tk
import webbrowser

window = Tk()
window.geometry("500x500")
window.title("Test")

#txt_comentario = "text text text"

panelF = PanedWindow(window, width=610, height=480, relief="sunken", bd="3")
panelF.place(x=100, y=50)

tree3=ttk.Treeview(panelF, height=40, selectmode="browse",columns=("Nome","Tipo","Estado"), show="headings")
tree3.column("Nome", width=200, anchor="c")
tree3.column("Tipo", width=200, anchor="c")
tree3.column("Estado", width=200, anchor="c")
tree3.heading("Nome", text="Nome")
tree3.heading("Tipo", text="Tipo")
tree3.heading("Estado", text="Estado")
tree3.place(x=1, y=1)

nome_selecao = tree3
username = "nini1"
spin = 6

button = Button(window,height=3, width=10, text=">", command = lambda: tree_favoritos(nome_selecao, username))
button.place(x=20, y=20)

def tree_favoritos(tree3: Treeview, username):
    tree3.delete(*tree3.get_children())
    catalogo = open("Catalogo.txt", "r", encoding ="UTF-8")
    lista_c = catalogo.readlines()
    favoritos = open("Favoritos.txt", "r", encoding ="UTF-8")
    lista_f = favoritos.readlines()
    vistos = open("Vistos.txt", "r", encoding="UTF-8")
    lista_v = vistos.readlines()
    for line in lista_f:
        campos = line.split(";")
        if campos[0] == username:
            for i in range(1,len(campos)):
                filme = campos[i]
                for linha in lista_c:
                    campos_c = linha.split(";")
                    if campos_c[0] == filme or campos_c[0]+"\n" == filme:
                        tipo = campos_c[2]
                        break
                for linha in lista_v:
                    campos_v = linha.split(";")
                    if campos_v[0] == username and (filme in campos_v or (filme+"\n") in campos_v):
                        estado = "Visto"
                        break
                    else:
                        estado = "Não visto"
                        break
                tree3.insert("", "end", values = (filme,tipo,estado))


window.mainloop()