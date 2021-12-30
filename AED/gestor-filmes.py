#Beatriz Rodrigues, nº aluno:
#Daniela Moreira, nº aluno:40210349
#Daniela Monteiro, nº aluno:40210288

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
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

app_width = 700
app_height = 500

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
window.title("Projeto de Algoritmia")

original_frame=window
#App(window)

def login_entrar():
    window2=Tk()
    screen_width = window2.winfo_screenwidth()
    screen_height = window2.winfo_screenheight()

    app_width = 350
    app_height = 250

    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    
    window2.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))

    window2.title("Login")
    window2.focus_force()
    window2.grab_set 

    #inserir dados
    lbl_email=Label(window2, text="Email:", font=("Helvetica", 9))
    lbl_email.place(x=60, y=50)

    lbl_password=Label(window2, text="Password:", font=("Helvetica", 9))
    lbl_password.place(x=60, y=90)

    txt_email=Entry(window2, width=20)
    txt_email.place(x=150, y=50)

    txt_password=Entry(window2, width=20, show="*")
    txt_password.place(x=150,y=90)

    btn_entrar=Button(window2, text="Entrar", width=10, height=2, relief="raised")
    btn_entrar.place(x=140, y=150)

def login_registar():
    window3=Tk()
    screen_width = window3.winfo_screenwidth()
    screen_height = window3.winfo_screenheight()

    app_width = 450
    app_height = 350

    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    
    window3.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))

    window3.title("Login")
    window3.focus_force()
    window3.grab_set 

    #inserir dados
    lbl_email=Label(window3, text="Email:", font=("Helvetica", 9))
    lbl_email.place(x=95, y=60)

    txt_email=Entry(window3, width=30)
    txt_email.place(x=180, y=60)

    lbl_username=Label(window3, text="Username:", font=("Helvetica", 9))
    lbl_username.place(x=95, y=100)

    txt_username=Entry(window3, width=30)
    txt_username.place(x=180, y=100)

    lbl_password=Label(window3, text="Password:", font=("Helvetica", 9))
    lbl_password.place(x=95, y=140)

    txt_password=Entry(window3, width=30)
    txt_password.place(x=180, y=140)

    btn_registar=Button(window3, text="Registar", width=10, height=2, relief="raised")
    btn_registar.place(x=180, y=200)


def barraMenu():
    #cria barra menu
    barra=Menu()

    #opçoes de filmes
    opcoes_filmes=Menu(barra)
    opcoes_filmes.add_command(label="Catálogo de Filmes", command="noaction")
    opcoes_filmes.add_command(label="Top de Filmes")
    barra.add_cascade(label="Filmes", menu=opcoes_filmes)

    #opçoes de series
    opcoes_series=Menu(barra)
    opcoes_series.add_command(label="Catálogo de Séries", command="noaction")
    opcoes_series.add_command(label="Top de Séries", command="noaction")
    barra.add_cascade(label="Séries", menu=opcoes_series)

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
    barra.add_cascade(label="Géneros", menu=categorias)

    barra.add_command(label="Favoritos")
    
    #login
    opcoes_login=Menu(barra)
    opcoes_login.add_command(label="Entrar", command=login_entrar)
    opcoes_login.add_command(label="Registar", command=login_registar)
    barra.add_cascade(label="Login", menu=opcoes_login)

    barra.add_command(label="Sair", command=window.quit)

    window.configure(menu=barra)

barraMenu()

def filme(self):
    self.top=Toplevel()
    self.top.geometry("700x500")
    self.top.title("Login")
    self.top.focus_force()  

    lblFilme=Label(self.top, text="Titulo", font=("Helvetica",15))
    lblFilme.place(x=20, y=30)


window.mainloop()