#Beatriz Rodrigues, nº aluno:
#Daniela Moreira, nº aluno: 40210349
#Daniela Monteiro, nº aluno: 40210288
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk,Image
import os

window = Tk()
scrn_width = window.winfo_screenwidth()
scrn_height = window.winfo_screenheight()
app_w = 1000
app_h = 600
x=(scrn_width/2)-(app_w/2)
y=(scrn_height/2)-(app_h/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}".format(app_w,app_h,int(x),int(y)))
window.title('Gestor de filmes e séries')
'''????
lista_filmes =[]
lista_categorias=[]'''

def catalogo():
    n=1
def favoritos():
    wFavoritos = Tk()
    wFavoritos.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}".format(app_w,app_h,int(x),int(y)))
    wFavoritos.title('Gestor de filmes e séries')
    wFavoritos.focus_force()
    wFavoritos.grab_set()
    pannel1 = PanedWindow()

def log_in():
    n=1
def sair():
    res = messagebox.askquestion("Sair","Deseja sair?")
    if res=="yes":
        window.destroy()

#menu
main_menu = Menu(window)
main_menu.add_command(label="Catálago", command=catalogo)
main_menu.add_command(label="Favoritos", command=favoritos)
main_menu.add_command(label="Login", command=log_in)
main_menu.add_command(label="Sair", command=sair)
#main window
canvas = Canvas(window, width=400, height=200, relief="raised", bd=1)
canvas.place(x=200, y=150)
#IMAGEM
label = Label(window, text="Gestor de\nfilmes e séries", fg="red", font=("Helvitica, 20"))
label.place(x=650, y=200)

window.configure(menu=main_menu)

window.mainloop()