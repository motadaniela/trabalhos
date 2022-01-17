#Beatriz Rodrigues, nº aluno:40210313
#Daniela Moreira, nº aluno:40210349
#Daniela Monteiro, nº aluno:40210288

from cgitb import text
from distutils import command
from optparse import Values
from tkinter import *
from tkinter import ttk
from tokenize import String
from turtle import width
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.ttk import Combobox
import tkinter as tk

ficheiro="catalogo.txt"
acc=0   #conta nao iniciada

#cria janela centrada 
window=tk.Tk()
global screen_height
global screen_width
global app_height, app_width
global x, y
global username

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

app_width = 1000
app_height = 600

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
window.title("Projeto de Algoritmia")

def check_data(Email: Entry, Password: Entry, window2: Misc,acc):
    userdata = open("userdata.txt", "r")     #abre o ficheiro para leitura
    line = userdata.readline()
    for line in userdata:
        user_info = line.split(";")
        if user_info[3] == "admin\n" and user_info[0] == str(Email.get()) and user_info[1] == str(Password.get()):
            acc=2
            username = user_info[2]
            messagebox.showinfo("Bem vindo!","Bem vindo, " + user_info[2]+"!")
            barra_admin(barra_menu)
            userdata.close()
            break
        elif user_info[3]=="user\n" and user_info[0] == str(Email.get()) and user_info[1] == str(Password.get()):
            acc=1
            username = user_info[2]
            messagebox.showinfo("Bem vindo!","Bem vindo, " + user_info[2]+"!")
            barra_user(barra_menu)
            userdata.close()
            break
    if user_info[0]==Email.get() and user_info[1]!=Password.get():
        msg=Message(window2, text="Email ou password estão errados!", fg="red")
        msg.place(x=100, y=200)
    return(username,acc)

#entrar na conta
def login_entrar(barra_menu: Menu,acc):
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

    btn_entrar=Button(window2, text="Entrar", width=10, height=2, relief="raised", command=lambda:check_data(txt_email,txt_password,window2,acc))
    btn_entrar.place(x=140, y=150)

#funcao que verifica os dados de um novo utilizador para se registar
def newuser(window3: Misc,Email: Entry,Username: Entry,Password: Entry,Password2,acc):
    if str(Password.get())!=str(Password2.get()):
        msg=Message(window3, text="Por favor confirme que a password coincide!", fg="red")
        msg.place(x=300, y=250)
    elif Email.get().rfind("@") == -1:
        msg=Message(window3, text="Email inválido!", fg="red")
        msg.place(x=300, y=250)
    else:
        userdata=open("userdata.txt", "r")
        line=userdata.readlines()
        userdata.close()
        for i in range(len(line)):
            user_info=line[i].split(";")
            if str(user_info[0]) == str(Email.get()):
                msg=Message(window3, text="Esse email já está em uso, escolha outro!", fg="red")
                msg.place(x=300, y=250)
                break   
            elif str(user_info[2]) == str(Username.get()):
                msg=Message(window3, text="Username já existe, escolha outro!", fg="red")
                msg.place(x=300, y=250)
                break
        else:
            data=open("userdata.txt", "a")
            data.write(Email.get()+";"+Password.get()+";"+Username.get())
            if acc==2:
                data.write(";admin\n")
                data.close()
                messagebox.showinfo("Novo admin","Nova conta admin criada!")
                window3.destroy()
                return(Username.get())
            elif acc==0:
                data.write(";user\n")
                data.close()
                messagebox.showinfo("Bem vindo!","Bem vindo, " + Username.get() + "!")
                barra_user(barra_menu)
                return(Username.get())


#registar
def login_registar(acc):
    window3=tk.Toplevel()
    screen_width = window3.winfo_screenwidth()
    screen_height = window3.winfo_screenheight()

    app_width = 450
    app_height = 350

    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    
    window3.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))

    window3.title("Registar")
    window3.focus_force()
    window3.grab_set 

    #inserir dados
    lbl_email=Label(window3, text="Email:", font=("Helvetica", 9))
    lbl_email.place(x=70, y=60)

    txt_email=Entry(window3, width=30)
    txt_email.place(x=190, y=60)

    lbl_username=Label(window3, text="Username:", font=("Helvetica", 9))
    lbl_username.place(x=70, y=100)

    txt_username=Entry(window3, width=30)
    txt_username.place(x=190, y=100)

    lbl_password=Label(window3, text="Password:")
    lbl_password.place(x=70, y=140)

    txt_password=Entry(window3, width=30, show="*")
    txt_password.place(x=190, y=140)

    lbl_password2=Label(window3, text="Confirme password:")
    lbl_password2.place(x=70, y=180)

    txt_password2=Entry(window3, width=30, show="*")
    txt_password2.place(x=190, y=180)

    btn_registar=Button(window3, text="Registar", width=10, height=2, relief="raised", command=lambda:newuser(window3,txt_email,txt_username,txt_password,txt_password2,acc))
    btn_registar.place(x=180, y=220)

def logout(acc):
    acc=0
    barraMenu()
    return acc

#funcao que pede para confirmar que a intensao do utilizador é sair
def sair():
    res = messagebox.askquestion("Sair","Deseja sair?")
    if res=="yes":
        window.destroy()

#barra para o admin
def barra_admin(barra_menu: Menu):
    barra_menu.delete(3)
    barra_menu.delete(2)
    barra_menu.add_command(label="Adicionar", command=adicionar)
    barra_menu.add_command(label="Log out", command=lambda: logout(acc))
    barra_menu.add_command(label="Novo admin", command=lambda: login_registar(acc))
    barra_menu.add_command(label="Sair", command=sair)

def barra_user(barra_menu: Menu):
    barra_menu.delete(3)
    barra_menu.delete(2)
    barra_menu.add_command(label="Favoritos", command=favoritos)
    barra_menu.add_command(label="Log out", command=lambda: logout(acc))
    barra_menu.add_command(label="Sair", command=sair)
    return

#barra menu principal
def barraMenu():
    #cria barra menu
    barra=Menu()

    #opçoes de filmes
    barra.add_command(label="Catálogo", command=catalogo)
    
    #login
    opcoes_login=Menu(barra)
    opcoes_login.add_command(label="Entrar", command=lambda:login_entrar(barra,acc))
    opcoes_login.add_command(label="Registar", command=lambda:login_registar(acc))
    barra.add_cascade(label="Login", menu=opcoes_login)

    barra.add_command(label="Sair", command=sair)

    window.configure(menu=barra)
    return barra

#catalogo de filmes e series 
#temos de adicionar masi filtros e mudar a aparencia para ficar mais bonito
def catalogo():
    window4=Toplevel()   
    window4.title("Catálogo") 
    window4.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
    window4.focus_force()     
    window4.grab_set()

    #painel
    panel1=PanedWindow(window4, width=660, height=570, bd="3", relief="sunken")
    panel1.place(x=310, y=10)

    #acho que tenho de mudar o nome da tree
    #lista de filmes e series
    global tree2 
    tree2=ttk.Treeview(panel1, height=50, selectmode="browse",columns=("Nome","Ano","Tipologia","Categoria","Pontuação","Visualizações"), show="headings")
    tree2.column("Nome", width=160, anchor="c")
    tree2.column("Ano", width=100, anchor="c")
    tree2.column("Tipologia", width=100, anchor="c")
    tree2.column("Categoria", width=100, anchor="c")  #supostamente c é para centrar
    tree2.column("Pontuação", width=100, anchor="c")
    tree2.column("Visualizações", width=100, anchor="c")
    tree2.heading("Nome", text="Nome")
    tree2.heading("Ano", text="Ano")
    tree2.heading("Tipologia", text="Tipologia")
    tree2.heading("Categoria", text="Categoria")
    tree2.heading("Pontuação", text="Pontuação")
    tree2.heading("Visualizações", text="Visualizações")
    tree2.place(x=1, y=1)

    #painel
    panel2 = PanedWindow(window4, width = 220, height = 570, bd = "3", relief = "sunken")
    panel2.place(x=60, y=10) 

    #frame
    lframe = LabelFrame(panel2, width = 180, height=100, bd=3, text= "Filtrar por", fg = "blue", relief = "sunken")
    lframe.place(x=18, y=5)

    #filtar
    global vals
    global valf
    global val3     #variaveis globais para depois conseguir filtrar noutra funçao
    vals = IntVar()
    valf = IntVar()
    ck1 = Checkbutton(lframe, text = "Séries", variable = vals)
    ck1.place(x=15, y=15)
    ck2 = Checkbutton(lframe, text = "Filmes", variable = valf)
    ck2.place(x=15, y=40)

    #frame
    lframe2 = LabelFrame(panel2, width = 180, height=100, bd=3, text= "Pesquisar", fg = "blue", relief = "sunken")
    lframe2.place(x=18, y=110)
    lblUtilizador = Label(lframe2, text="Nome: ")
    lblUtilizador.place(x=15, y=10)

    val3 = StringVar()
    txtpesquisar = Entry(lframe2, width = 20, textvariable = val3)
    txtpesquisar.place(x=15, y=30)

    #frame generos
    lframe3 = LabelFrame(panel2, width=180, height=90, bd=3, text="Género", fg="blue", relief="sunken")
    lframe3.place(x=18, y=215)

    global cb_gen 
    cb_gen = StringVar()
    lista = ["Ação", "Animação", "Aventura", "Comédia", "Comédia Romântica", "Dança", "Documentário", "Drama", "Espionagem", "Faroeste", "Fantasia", "Ficção Científica", "Guerra", "Mistério", "Musical", "Policial", "Romance", "Terror", "Thriller"]
    cb_gen=Combobox(lframe3, values=lista)
    cb_gen.place(x=15, y=20)

    #frame ordenar
    lframe4 = LabelFrame(panel2, width=180, height=120, bd=3, text="Ordenar por", fg="blue", relief="sunken")
    lframe4.place(x=18, y=310)

    lbl_alf=Label(lframe4, text="Ordem alfabética")
    lbl_alf.place(x=35, y=6)
    btn_alf=Button(lframe4, width=2, height=1, relief="raised", bg="blue", command=sort_alf)
    btn_alf.place(x=8, y=5)

    lbl_vis=Label(lframe4, text="Visualizações")
    lbl_vis.place(x=35, y=38)
    btn_vis=Button(lframe4, width=2, height=1, relief="raised", bg="red", command=sort_vis)
    btn_vis.place(x=8, y=35)

    lbl_pont=Label(lframe4, text="Pontuação")
    lbl_pont.place(x=35, y=68)
    btn_pont=Button(lframe4, width=2, height=1, relief="raised", bg="green", command=sort_pont)
    btn_pont.place(x=8, y=65)


    #botões
    btnpesquisar = Button(panel2, width = 24, height= 2, text = "Pesquisar", relief = "raised", command =dados_treeview)
    btnpesquisar.place(x=18, y=430)

    btn_abrir = Button(panel2, width = 24, height = 2, text = "Mais Informações", relief = "raised", command=lambda:selecionar(tree2))
    btn_abrir.place(x=18, y=475)

    btn_fav = Button(panel2, width = 24, height=2, text= "Adicionar aos Favoritos", relief = "raised")
    btn_fav.place(x=18, y=520)



#isto é para filtar os dados da tree mas ainda nao funciona
#copiei do ex11
def dados_treeview():  # Remove TODAS as linhas da Treeview
    tree2.delete(*tree2.get_children())
    tipo = ""
    if vals.get() == True and valf.get() == True:   # Se está checado serie e filme (vals e valf)
        tipo = "T"
    elif vals.get() == True: # serie checado
        tipo = "Série"
    elif valf.get() == True: # filme checado
        tipo = "Filme"
    elif vals.get() == False and valf.get() == False:  #nada selecionado -> catálogo todo 
        f=open(ficheiro, "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            tree2.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3],campos[4], campos[5]))                 
    
    f = open(ficheiro, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    for linha in lista:
        campos = linha.split(";")
        if tipo == "T" or campos[2] == tipo:
            if val3.get() == "" or val3.get() == campos[0]:
                if cb_gen.get() == "" or cb_gen.get() == campos[3]:
                    tree2.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3],campos[4], campos[5]))
        
def sort_alf():
    linhas = [(tree2.item(item,"values"), item) for item in tree2.get_children('')]
    print(linhas)
    linhas.sort()
    print(linhas)

    for index, (values, item) in enumerate(linhas):
        tree2.move(item,'',index)

def sort_vis():
    linhas = [(tree2.item(item,"values"), item) for item in tree2.get_children('')]
    linhas.sort(key=lambda linhas:linhas[0][5])
    for index, (values, item) in enumerate(linhas):
        tree2.move(item,'',index)

def sort_pont():
    linhas = [(tree2.item(item,"values"), item) for item in tree2.get_children('')]
    linhas.sort(key=lambda linhas:linhas[0][4])
    for index, (values, item) in enumerate(linhas):
        tree2.move(item,'',index)        
        
#n esta a mostrar n sei pq
#página de favoritos + visto ou nao visto
def favoritos(acc):
    wFavoritos=Toplevel()
    wFavoritos.title("Favoritos") 
    wFavoritos.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
    wFavoritos.focus_force()     
    wFavoritos.grab_set()

    panelF = PanedWindow(wFavoritos, width=610, height=480, relief="sunken", bd="3")
    panelF.place(X=100, y=50)

    tree=ttk.Treeview(panelF, height=40, selectmode="browse",columns=("Nome","Ano","Tipologia","Categoria","Pontuação","Visualizações"), show="headings")
    tree.column("Nome", width=300, anchor="c")
    tree.column("Tipo", width=300, anchor="c")
    tree.column("Estado", width=300, anchor="c")
    tree.heading("Nome", text="Nome")
    tree.heading("Tipo", text="Tipo")
    tree.heading("Estado", text="Estado")
    tree.place(x=1, y=1)

    #botoes
    bttn_remover=Button(wFavoritos, text="Remover", width=30, height=3)
    bttn_remover.place(x=110, y=510)
    bttn_visto=Button(wFavoritos, text="Visto", width=30, height=3)
    bttn_visto.place(x=200, y=510)
    bttn_nvisto=Button(wFavoritos, text="Não Visto", width=30, height=3)
    bttn_nvisto.place(x=290, y=510)


#remove linha
#selecionas uma linha no catalogo do admin e carregas em remover
def remover(window5):
    selecao=tree.focus()
    selecao=int(selecao[1:],16)
    i=0
    with open(ficheiro, "r", encoding="UTF-8") as f:
        new_text=""
        for line in f:
            i+=1
            filme=line.split(";")
            if selecao==i:
                print("removido")
            else:
                new_text=new_text+line
    with open(ficheiro, "w", encoding="UTF-8") as f:
        f.write(new_text)
    window5.destroy()
    adicionar()
    
#mostra os dados anteriores
def mostrar():
    tree.delete(*tree.get_children())
    f = open(ficheiro, "r", encoding="utf-8")
    lista=f.readlines()
    f.close()
    for linha in lista:
        campos = linha.split(";")
        tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3])) 

#adicionar filme/serie  
def adicionar_linha():
    f = open(ficheiro, "a", encoding="utf-8")
    nome2 = nome.get()
    ano2 = str(ano.get())
    tipologia2 = tipologia.get()
    categoria2 = categoria.get()
    linha = nome2 + ";" +ano2+ ";" +tipologia2+ ";" +categoria2+";0;0"+ "\n" 
    campos = linha.split(";")
    f.write(linha)
    f.close()
    tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3]))

#adicionar pagina
def adicionar():
    window5 = Toplevel()   
    window5.title("Adicionar ao catalogo") 
    window5.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
    window5.focus_force()    
    window5.grab_set()       
             
    
    #Button
    btnadicionar = Button(window5, width = 10, height= 2, text = "Adicionar", fg="blue", command =adicionar_linha)
    btnadicionar.place(x=400, y=550)

    btnremover = Button(window5, width = 10, height= 2, text = "Remover", fg="red",command=lambda:remover(window5))
    btnremover.place(x=500, y=550)

    lbladicionar = Label(window5, text="Adicionar novo filme/série")
    lbladicionar.place(x=30, y=420)

    global nome
    nome=StringVar()
    lblnome = Label(window5, text="Nome")
    lblnome.place(x=200, y=450)
    txtnome = Entry(window5, width = 20, textvariable=nome)
    txtnome.place(x=160, y=500)

    global ano
    ano=IntVar()
    lblano = Label(window5, text="Ano")
    lblano.place(x=350, y=450)
    txtano = Entry(window5, width = 20, textvariable=ano)
    txtano.place(x=310, y=500)

    global tipologia
    tipologia=StringVar()
    lbltipologia = Label(window5, text="Tipologia")
    lbltipologia.place(x=470, y=450)
    txttipologia = Entry(window5, width = 20, textvariable=tipologia)
    txttipologia.place(x=450, y=500)

    global categoria
    categoria=StringVar()
    lblcategoria = Label(window5, text="Categoria")
    lblcategoria.place(x=620, y=450)
    txtcategoria = Entry(window5, width = 20, textvariable=categoria)
    txtcategoria.place(x=600, y=500)

    # Panel
    panel1 = PanedWindow(window5, width = 950, height = 400, bd = "3", relief = "sunken")
    panel1.place(x=10, y=10)
    #ListBox
    global tree  
    tree=ttk.Treeview(panel1,height=17,selectmode="browse",columns=("Nome","Ano","Tipologia","Categoria"), show="headings")
    tree.column("Nome", width=240, anchor="c")
    tree.column("Ano", width=230, anchor="c")
    tree.column("Tipologia", width=230, anchor="c")
    tree.column("Categoria", width=230, anchor="c")
    tree.heading("Nome", text="Nome")
    tree.heading("Ano", text="Ano")
    tree.heading("Tipologia", text="Tipologia")
    tree.heading("Categoria", text="Categoria")
    tree.place(x=1, y=1)
    mostrar()

def selecionar(tree2):
    selecao=tree2.focus()
    selecao=int(selecao[1:],16)
    i=0
    with open(ficheiro, "r", encoding="UTF-8") as f:
        new_text=""
        for line in f:
            filme=line.split(";")
    mais_informacoes()
        

def mais_informacoes():
    window6=Toplevel()   
    window6.title("Informações") 
    window6.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
    window6.focus_force()     
    window6.grab_set()

    lbl_poster=Label(window6, text="blablabla", font=("Helvetica",20))
    lbl_poster.place(x=10,y=10)

    poster_canvas=Canvas(window6, width=240, height=340, bd=2, relief="sunken" )
    poster_canvas.place(x=10,y=50)

    lbl_avaliar=Label(window6, text="Avalie de 0 a 5:", font=("Helvetica",20))
    lbl_avaliar.place(x=10,y=10)

    lista_num=[0,1,2,3,4,5]
    spin=Spinbox(window6, width=10, values=lista_num)
    spin.place(x=300,y=200)

    


barra_menu = barraMenu()

#foto
background_image=ImageTk.PhotoImage(Image.open("background.jpg"))
background_label = tk.Label(image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

lbl = Label(window, text = "Gestor de Filmes", bg="#ffc04f", font = ("Cambria", 50))
lbl.place(x=120, y=320)

window.mainloop()