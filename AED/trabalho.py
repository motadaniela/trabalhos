#Beatriz Rodrigues, nº aluno: 40210313
#Daniela Moreira, nº aluno: 40210349
#Daniela Monteiro, nº aluno: 40210288
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog
from PIL import ImageTk,Image
import os

window = Tk()
scrn_width = window.winfo_screenwidth()
scrn_height = window.winfo_screenheight()
app_w = 700
app_h = 500
x=(scrn_width/2)-(app_w/2)
y=(scrn_height/2)-(app_h/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}".format(app_w,app_h,int(x),int(y)))
window.title('Gestor de filmes e séries')
'''????
lista_filmes =[]
lista_categorias=[]'''

def catalogo():
    wCatalogo = Toplevel()
    scrn_width = wCatalogo.winfo_screenwidth()
    scrn_height = wCatalogo.winfo_screenheight()
    app_width = 700
    app_height = 500
    x = (scrn_width/2) - (app_width/2)
    y = (scrn_height/2) - (app_height/2)
    wCatalogo.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
    wCatalogo.title("Catálogo")
    wCatalogo.focus_force()
    wCatalogo.grab_set

def favoritos():
    wFavoritos = Toplevel()
    scrn_width = wFavoritos.winfo_screenwidth()
    scrn_height = wFavoritos.winfo_screenheight()
    app_width = 700
    app_height = 500
    x = (scrn_width/2) - (app_width/2)
    y = (scrn_height/2) - (app_height/2)
    wFavoritos.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
    wFavoritos.title("Favoritos")
    wFavoritos.focus_force()
    wFavoritos.grab_set
    pannel1 = PanedWindow(wFavoritos)

def iniciar_sessao():
    wlogin = Toplevel()
    screen_width = wlogin.winfo_screenwidth()
    screen_height = wlogin.winfo_screenheight()
    app_width = 300
    app_height = 300
    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    wlogin.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
    wlogin.title("Login")
    wlogin.resizable(0,0)
    wlogin.focus_force()
    wlogin.grab_set

    lbl_email = Label(wlogin, text="Email:")
    lbl_email.place(x=40, y=50)
    email = Entry(wlogin, width=20)
    email.place(x=110, y=50)
    lbl_password = Label(wlogin, text="Password:")
    lbl_password.place(x=40, y=100)
    password = Entry(wlogin, width=20)
    password.place(x=110, y=100)

    def login():
        n=1

    bttn = Button(wlogin, text="Entrar", width=10, height=1, command=login)
    bttn.place(x=100, y=180)

    wlogin.mainloop()

def registar():
    wlogin = Toplevel()
    screen_width = wlogin.winfo_screenwidth()
    screen_height = wlogin.winfo_screenheight()
    app_width = 300
    app_height = 300
    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    wlogin.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
    wlogin.title("Login")
    wlogin.resizable(0,0)
    wlogin.focus_force()
    wlogin.grab_set

    lbl_email = Label(wlogin, text="Email:")
    lbl_email.place(x=40, y=50)
    email = Entry(wlogin, width=20)
    email.place(x=110, y=50)
    lbl_username = Label(wlogin, text="User name:")
    lbl_username.place(x=40, y=100)
    username = Entry(wlogin, width=20)
    username.place(x=110, y=100)
    lbl_password = Label(wlogin, text="Password:")
    lbl_password.place(x=40, y=150)
    password = Entry(wlogin, width=20)
    password.place(x=110, y=150)

    def new_user():
        n=1

    bttn = Button(wlogin, text="Registar", width=10, height=1, command=new_user)
    bttn.place(x=100, y=200)

    wlogin.mainloop()

def sair():
    res = messagebox.askquestion("Sair","Deseja sair?")
    if res=="yes":
        window.destroy()

#menu
main_menu = Menu(window)
main_menu.add_command(label="Catálago", command=catalogo)
main_menu.add_command(label="Favoritos", command=favoritos)
log_in = Menu(main_menu)
log_in.add_command(label="Iniciar sessao", command=iniciar_sessao)
log_in.add_command(label="Registar", command=registar)
main_menu.add_cascade(label="Log in", menu=log_in)
main_menu.add_command(label="Sair", command=sair)

#main window
canvas = Canvas(window, width=300, height=200, relief="raised", bd=1)
canvas.place(x=100, y=100)
#IMAGEM
label = Label(window, text="Gestor de\nfilmes e séries", fg="red", font=("Helvitica, 20"))
label.place(x=450, y=150)

window.configure(menu=main_menu)

window.mainloop()