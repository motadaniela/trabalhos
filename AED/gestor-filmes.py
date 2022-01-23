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
window6=tk.Tk()
global screen_height
global screen_width
global app_height, app_width
global x, y
global username

screen_width = window6.winfo_screenwidth()
screen_height = window6.winfo_screenheight()

app_width = 1000
app_height = 600

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

window6.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
window6.title("Gestor de Filmes e Séries")



def mais_informacoes():
    window6=Toplevel()   
    window6.title("Informações") 
    window6.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
    window6.focus_force()     
    window6.grab_set()

    lbl_poster=Label(window6, font=("Helvetica",20))
    lbl_poster.place(x=10,y=10)

    poster_canvas=Canvas(window6, width=240, height=340, bd=2, relief="sunken" )
    poster_canvas.place(x=10,y=50)


    lbl_avaliar=Label(window6, text="Avalie de 0 a 5:", font=("Helvetica",11))
    lbl_avaliar.place(x=320,y=340)

    lista_num=[0,1,2,3,4,5]
    spin=Spinbox(window6, width=10, values=lista_num)
    spin.place(x=335,y=370)

    btn_video=Button(window6, text="Ver trailer", height=2, command=lambda:playVideo(), font=("Helvetica",15))
    btn_video.place(x=300,y=50)

    btn_fav=Button(window6, text="Adicionar aos Favoritos", height=2)
    btn_fav.place(x=500,y=340)

    lbl_sipnose=Label(window6, text="Sipnose", font=("Helvetica",18))
    lbl_sipnose.place(x=800,y=50)
    
    msg_sinopse=Message(window6, font=("Helvetica",12), bg="white")
    msg_sinopse.place(x=750, y=80)

    lbl_comentario=Label(window6, text="Deixe um comentário!", font=("Helvetica",11))
    lbl_comentario.place(x=10,y=420)

    txt_comentario=Text(window6, width=30,height=5, wrap="word")
    txt_comentario.place(x=10,y=450)

   

    def playVideo(link_selecao):
        url=link_selecao
        webbrowser.open(url,new=0,autoraise=True)

mais_informacoes()

window6.mainloop()