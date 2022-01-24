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
from tkinter.ttk import Combobox
import tkinter as tk
import webbrowser

ficheiro="catalogo.txt"
acc=0   #conta nao iniciada

#cria janela centrada 
wFavoritos=tk.Tk()
global screen_height
global screen_width
global app_height, app_width
global x, y
global username

screen_width = wFavoritos.winfo_screenwidth()
screen_height = wFavoritos.winfo_screenheight()

app_width = 1000
app_height = 600

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

wFavoritos.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
wFavoritos.title("Gestor de Filmes e Séries")






panelF = PanedWindow(wFavoritos, width=610, height=480, relief="sunken", bd="3")
panelF.place(x=100, y=50)

tree3=ttk.Treeview(panelF, height=40, selectmode="browse",columns=("Nome","Tipo","Estado"), show="headings")
tree3.column("Nome", width=200, anchor="c")
tree3.column("Tipo", width=200, anchor="c")
tree3.column("Estado", width=200, anchor="c")
tree3.heading("Nome", text="Nome")
tree3.heading("Tipo", text="Tipo")
tree3.heading("Estado", text="Estado")
tree3.place(x=1, y=1)

#botoes
bttn_remover=Button(wFavoritos, text="Remover", width=30, height=3)
bttn_remover.place(x=750, y=100)
bttn_visto=Button(wFavoritos, text="Visto", width=30, height=3)
bttn_visto.place(x=750, y=250)
bttn_nvisto=Button(wFavoritos, text="Não Visto", width=30, height=3)
bttn_nvisto.place(x=750, y=400)



wFavoritos.mainloop()