#Beatriz Rodrigues, nº aluno:40210313
#Daniela Moreira, nº aluno:40210349
#Daniela Monteiro, nº aluno:40210288

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk,Image 
from tkinter.ttk import Combobox
import tkinter as tk
import os


#cria janela
window=tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

app_width = 700
app_height = 500

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
window.title("Projeto de Algoritmia")



def login_entrar():
    window2=tk.Toplevel()
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
    window3=tk.Toplevel()
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

    barra.add_command(label="Pesquisar", command=lambda:pesquisar())

    #opçoes de filmes
    opcoes_filmes=Menu(barra)
    opcoes_filmes.add_command(label="Catálogo de Filmes", command=lambda:filmes())
    #opcoes_filmes.add_command(label="Top de Filmes", command=lambda:filmes())
    barra.add_cascade(label="Filmes", menu=opcoes_filmes)

    #opçoes de series
    opcoes_series=Menu(barra)
    opcoes_series.add_command(label="Catálogo de Séries", command=lambda:series())
    #opcoes_series.add_command(label="Top de Séries", command="noaction")
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


def pesquisar():
    barraMenu()

    lblpesquisar=Label(window, text="Pesquisar:", fg="red", font=("Helvetica", 18))
    lblpesquisar.place(x=280, y=130)

    txtpesquisar=Text(window, width=30, height=1, wrap="word")
    txtpesquisar.place(x=215, y=180)

    lblfiltros=Label(window, text="Filtrar por:", font=("Helvetica", 9))
    lblfiltros.place(x=300, y=250)

    selected=IntVar()
    radnenhum=Radiobutton(window, text="Nenhum",variable="selected",value="Nenhum")
    radfilmes=Radiobutton(window,text="Filmes", variable="selected",value="Filmes")
    radseries=Radiobutton(window,text="Séries", variable="selected",value="Séries")

    radnenhum.place(x=200,y=300)
    radfilmes.place(x=300,y=300)
    radseries.place(x=400,y=300)

    btnpesquisar=Button(window, text="Pesquisar", state="active")
    btnpesquisar.place(x=300, y=370)

def filmes():
    window4=tk.Toplevel()
    screen_width = window4.winfo_screenwidth()
    screen_height = window4.winfo_screenheight()

    app_width = 700
    app_height = 500

    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    
    window4.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))

    window4.title("Login")
    window4.focus_force()
    window4.grab_set 

    catalogo(window4)

    lblpesquisar=Label(window4, text="Pesquisar:", fg="red", font=("Helvetica", 9))
    lblpesquisar.place(x=20, y=20)

    txtpesquisar=Text(window4, width=20, height=1, wrap="word")
    txtpesquisar.place(x=100, y=20)

    btnok=Button(window4, text="OK", state="active")
    btnok.place(x=280, y=18)

    lblordenar=Label(window4, text="Ordenar por:", fg="red", font=("Helvetica", 9))
    lblordenar.place(x=470, y=20)

    cb_ordenar=Combobox(window4,values=lista)
    cb_ordenar.place(x=550, y=20)

    

    

def series():
    window5=tk.Toplevel()
    screen_width = window5.winfo_screenwidth()
    screen_height = window5.winfo_screenheight()

    app_width = 700
    app_height = 500

    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    
    window5.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))

    window5.title("Login")
    window5.focus_force()
    window5.grab_set 

    lblpesquisar=Label(window5, text="Pesquisar:", fg="red", font=("Helvetica", 9))
    lblpesquisar.place(x=20, y=20)

    txtpesquisar=Text(window5, width=20, height=1, wrap="word")
    txtpesquisar.place(x=100, y=20)

    btnok=Button(window5, text="OK", state="active")
    btnok.place(x=280, y=18)

    lblordenar=Label(window5, text="Ordenar por:", fg="red", font=("Helvetica", 9))
    lblordenar.place(x=470, y=20)

    cb_ordenar=Combobox(window5,values=lista)
    cb_ordenar.place(x=550, y=20)
    

def catalogo(window4):
   ctn_canvas=Canvas(window4,width=100, height=150, bd=2, relief="sunken")
   ctn_canvas.place(x=20, y=60)
   img=ImageTk.PhotoImage(Image.open("cantar2.JPG"))
   ctn_canvas.create_image(50,75, image=img) 







lista=["Pontuação", "Visualizações", "Ordem Alfabetica"]

barraMenu()

pesquisar()



window.mainloop()