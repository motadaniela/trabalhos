#Beatriz Rodrigues, nº aluno:40210313
#Daniela Moreira, nº aluno:40210349
#Daniela Monteiro, nº aluno:40210288

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk,Image 
from tkinter.ttk import Combobox
import tkinter as tk

ficheiro="catalogo.txt"

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


    #opçoes de filmes
    barra.add_command(label="Catalogo", command=filmes)

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




def filmes():
    window4=tk.Toplevel()
    screen_width = window4.winfo_screenwidth()
    screen_height = window4.winfo_screenheight()

    app_width = 700
    app_height = 500

    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    
    window4.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))

    window4.title("Filmes")
    window4.focus_force()
    window4.grab_set 

    catalogo(window4)


    

def catalogo(window4):
    #painel
    panel1=PanedWindow(window4, width=450, height=270, bd="3", relief="sunken")
    panel1.place(x=220, y=20)

    #lista de filmes e series
    global tree  
    tree=ttk.Treeview(panel1, selectmode="browse",columns=("Nome","Ano","Pontuação","Visualizações"), show="headings")
    tree.column("Nome", width=140, anchor="c")
    tree.column("Ano", width=100, anchor="c")
    tree.column("Pontuação", width=100, anchor="c")
    tree.column("Visualizações", width=100, anchor="c")
    tree.heading("Nome", text="Nome")
    tree.heading("Ano", text="Ano")
    tree.heading("Pontuação", text="Pontuação")
    tree.heading("Visualizações", text="Visualizações")
    tree.place(x=5, y=5)

    #painel
    panel2 = PanedWindow(window4, width = 200, height = 270, bd = "3", relief = "sunken")
    panel2.place(x=15, y=20) 

    #frame
    lframe = LabelFrame(panel2, width = 160, height=100, bd=3, text= "Filtrar por", fg = "blue", relief = "sunken")
    lframe.place(x=5, y=5)

    #filtar
    global vals
    global valf
    global val3
    vals = IntVar()
    valf = IntVar()
    ck1 = Checkbutton(lframe, text = "Séries", variable = vals)
    ck1.place(x=15, y=15)
    ck2 = Checkbutton(lframe, text = "Filmes", variable = valf)
    ck2.place(x=15, y=40)

    #frame
    lframe2 = LabelFrame(panel2, width = 160, height=100, bd=3, text= "Pesquisar", fg = "blue", relief = "sunken")
    lframe2.place(x=5, y=120)
    lblUtilizador = Label(lframe2, text="Nome: ")
    lblUtilizador.place(x=15, y=5)

    val3 = StringVar()
    txtpesquisar = Entry(lframe2, width = 20, textvariable = val3)
    txtpesquisar.place(x=15, y=25)

    btnpesquisar = Button(panel2, width = 21, height= 2, text = "Pesquisar", relief = "raised", command =dados_treeview)
    btnpesquisar.place(x=8, y=222)

def dados_treeview():  # Remove TODAS as linhas da Treeview
    tree.delete(*tree.get_children()) 
    mov = ""
    if vals.get() == True and valf.get() == True:   # Se está checado serie e filme (vals e valf)
        mov = "T"
    else:
        if vals.get() == True:                      # se está apenas checado vals (serie)
            mov = "Séries\n"
        if valf.get() == True:                      # se está apenas checado valf (filme)
            mov = "Filmes\n"
    f = open(ficheiro, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    for linha in lista:
        campos = linha.split(";")
        if mov == "T" or  campos[3] == mov:
            if val3.get() == "" or val3.get() == campos[0]:
                    tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3]))



barraMenu()




#foto
ctnCanvas = Canvas(window, width = 350, height = 200, bd = 4, relief = "sunken")
ctnCanvas.place(x=70, y=100)
imginicio = ImageTk.PhotoImage(Image.open("netflix.jpg"))
ctnCanvas.create_image(175,100, image = imginicio)

lbl = Label(window, text = "Gestor de Filmes", font = ("Helvetica", 12))
lbl.place(x=450, y=200)


window.mainloop()