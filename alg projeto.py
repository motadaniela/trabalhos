#eu nao consigo fazer esta porcaria e acho que é por causa das bibliotecas!!!!


from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed import self
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
#from PIL import ImageTk,Image 

#cria janela
window=Tk()
window.geometry("700x500")
window.title("Projeto de Algoritmia")

original_frame=window
#App(window)


def barraMenu():
    #cria barra menu
    barra=Menu()

    barra.add_command(label="Filmes")
    barra.add_command(label="Séries")

    #generos de filmes
    categorias=Menu(barra)
    categorias.add_command(label="Ação", command="noaction")
    categorias.add_command(label="Aventura", command="noaction")
    categorias.add_command(label="Comédia", command="noaction")
    categorias.add_command(label="Comédia Romântica", command="noaction")
    categorias.add_command(label="Dança", command="noaction")
    categorias.add_command(label="Documentario", command="noaction")
    categorias.add_command(label="Drama", command="noaction")
    categorias.add_command(label="Espionagem", command="noaction")
    categorias.add_command(label="Faroeste", command="noaction")
    categorias.add_command(label="Fantasia", command="noaction")
    categorias.add_command(label="Ficção Científica", command="noaction")
    categorias.add_command(label="Guerra", command="noaction")
    categorias.add_command(label="Mistério", command="noaction")
    categorias.add_command(label="Musical", command="noaction")
    categorias.add_command(label="Policial", command="noaction")
    categorias.add_command(label="Romance", command="noaction")
    categorias.add_command(label="Terror", command="noaction")
    categorias.add_command(label="Thriller", command="noaction")
    barra.add_cascade(label="Génros", menu=categorias)

    barra.add_command(label="Favoritos")
    barra.add_command(label="Login", command=lambda:login())

    window.configure(menu=barra)

barraMenu()

def login(self):
    self.original_frame.withdraw()

    self.top=Toplevel()
    self.top.geometry("700x500")
    self.top.title("Login")
    self.top.focus_force()  

    #barraMenu()

    lblUsername=Label(self.top, text="Username:", font=("Helvetica", 9))
    lblUsername.place(x=20, y=30)

    lblPassword=Label(self.top, text="Password:", font=("Helvetica", 9))
    lblPassword.place(x=20, y=70)

    txt_Username=Entry(self.top, width=20)
    txt_Username.place(x=100, y=30)

    txtPassword=Entry(self.top, width=20, show="*")
    txtPassword.place(x=100,y=70)

def filme(self):
    self.top=Toplevel()
    self.top.geometry("700x500")
    self.top.title("Login")
    self.top.focus_force()  

    lblFilme=Label(self.top, text="Titulo", font=("Helvetica",15))
    lblFilme.place(x=20, y=30)



window.mainloop()