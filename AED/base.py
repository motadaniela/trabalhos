#Beatriz Rodrigues, nº aluno:40210313
#Daniela Moreira, nº aluno:40210349
#Daniela Monteiro, nº aluno:40210288

from tkinter import *
from tkinter import ttk
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

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

app_width = 1000
app_height = 600

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
window.title("Projeto de Algoritmia")

def check_data(Email, Password, window2,acc):
    userdata = open("userdata.txt", "r")     #abre o ficheiro para leitura
    line = userdata.readline()
    for line in userdata:
        pos = line.index(";")
        search = line[0:int(line.index(";"))]     #procura o 1o elemento da linha(email)
        passe = line[pos+1:int(line.index(";", pos+1))]    #procura o 2o elemento da linha(password)
        if search == Email and passe == Password:
            username = line[line.index(";", pos+1)+1:line.index("\n")]
            messagebox("Bem Vindo!", "Bem vindo{0}!".format(username))
            acc=1
            break
        elif (search!=Email and passe==Password) or (search==Email and passe!=Password):
            msg=Message(window2, text="O email ou password estão errados!", fg="red")
            msg.place(x=100, y=200)
            break
        else:
            msg=Message(window2, text="Por favor registe-se", fg="red")
            msg.place(x=100, y=200)
            break
    userdata.close()
    return(username,acc)

#entrar na conta
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

    Email=txt_email.get()
    Password=txt_password.get()

    btn_entrar=Button(window2, text="Entrar", width=10, height=2, relief="raised", command=lambda:check_data(Email,Password,window2,acc))

    btn_entrar=Button(window2, text="Entrar", width=10, height=2, relief="raised")
    btn_entrar.place(x=140, y=150)

#registar mas ainda nao funciona
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

#funcao que pede para confirmar que a intensao do utilizador é sair
def sair():
    res = messagebox.askquestion("Sair","Deseja sair?")
    if res=="yes":
        window.destroy()

#barra em cima mas é so suposto aparecer adicionar para o admin
#tomos depois de mudar isso quando o login funcionar
def barraMenu():
    #cria barra menu
    barra=Menu()


    #opçoes de filmes
    barra.add_command(label="Catalogo", command=catalogo)

    barra.add_command(label="Favoritos", command=lambda:favoritos(acc))

    barra.add_command(label="Adicionar", command=adicionar)
    
    #login
    opcoes_login=Menu(barra)
    opcoes_login.add_command(label="Entrar", command=lambda:login_entrar())
    opcoes_login.add_command(label="Registar", command=lambda:login_registar())
    barra.add_cascade(label="Login", menu=opcoes_login)

    barra.add_command(label="Sair", command=sair)

    window.configure(menu=barra)

#catalogo de filmes e series 
#temos de adicionar masi filtros e mudar a aparencia para ficar mais bonito
def catalogo():
    window4=Toplevel()   
    window4.title("Catálogo") 
    window4.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
    window4.focus_force()     
    window4.grab_set()

    #painel
    panel1=PanedWindow(window4, width=610, height=480, bd="3", relief="sunken")
    panel1.place(x=220, y=20)

    #acho que tenho de mudar o nome da tree
    #lista de filmes e series
    tree2=ttk.Treeview(panel1, height=50, selectmode="browse",columns=("Nome","Ano","Tipologia","Categoria","Pontuação","Visualizações"), show="headings")
    tree2.column("Nome", width=100, anchor="c")
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
    panel2 = PanedWindow(window4, width = 200, height = 480, bd = "3", relief = "sunken")
    panel2.place(x=15, y=20) 

    #frame
    lframe = LabelFrame(panel2, width = 160, height=100, bd=3, text= "Filtrar por", fg = "blue", relief = "sunken")
    lframe.place(x=5, y=5)

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
    lframe2 = LabelFrame(panel2, width = 160, height=100, bd=3, text= "Pesquisar", fg = "blue", relief = "sunken")
    lframe2.place(x=5, y=110)
    lblUtilizador = Label(lframe2, text="Nome: ")
    lblUtilizador.place(x=15, y=5)

    val3 = StringVar()
    txtpesquisar = Entry(lframe2, width = 20, textvariable = val3)
    txtpesquisar.place(x=15, y=25)

    #frame generos
    lframe3 = LabelFrame(panel2, width=160, height=90, bd=3, text="Género", fg="blue", relief="sunken")
    lframe3.place(x=5, y=215)

    lista = ["Ação", "Aventura", "Comédia", "Comédia Romântica", "Dança", "Documentário", "Drama", "Espionagem", "Faroeste", "Fantasia", "Ficção Científica", "Guerra", "Mistério", "Musical", "Policial", "Romance", "Terror", "Thriller"]
    cb_gen=Combobox(lframe3, values=lista)
    cb_gen.place(x=5, y=20)

    btnpesquisar = Button(panel2, width = 21, height= 2, text = "Pesquisar", relief = "raised", command =dados_treeview)
    btnpesquisar.place(x=8, y=430)

    lframe4 = LabelFrame(panel2, width=160, height=120, bd=3, text="Ordenar por", fg="blue", relief="sunken")
    lframe4.place(x=5, y=310)

    selected=StringVar()
    rd1=Radiobutton(lframe4, text="Ordem alfabética", variable=selected, value="Ordem alfabética")
    rd1.place(x=5, y=5)
    rd2=Radiobutton(lframe4, text="Visualizações", variable=selected, value="Visualizações")
    rd2.place(x=5, y=35)
    rd3=Radiobutton(lframe4, text="Pontuação", variable=selected, value="Pontuação")
    rd3.place(x=5, y=65)

#n esta a mostrar n sei pq
#página de favoritos + visto ou nao visto
def favoritos(acc):
    #acc=1(só pus para ver a página)
    #caso sessao nao foi iniciada
    if acc==0:
        messagebox.showerror("Conta não iniciada","Por favor faça login!")
    elif acc==1:
        wFavoritos=Toplevel()
        wFavoritos.title("Favoritos") 
        wFavoritos.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
        wFavoritos.focus_force()     
        wFavoritos.grab_set()

        panelF = PanedWindow(wFavoritos, width=610, height=480, relief="sunken", bd="3")
        panelF.place(X=100, y=50)

        tree2=ttk.Treeview(panelF, height=40, selectmode="browse",columns=("Nome","Ano","Tipologia","Categoria","Pontuação","Visualizações"), show="headings")
        tree2.column("Nome", width=300, anchor="c")
        tree2.column("Tipo", width=300, anchor="c")
        tree2.column("Estado", width=300, anchor="c")
        tree2.heading("Nome", text="Nome")
        tree2.heading("Tipo", text="Tipo")
        tree2.heading("Estado", text="Estado")
        tree2.place(x=1, y=1)

        #botoes
        bttn_remover=Button(wFavoritos, text="Remover", width=30, height=3)
        bttn_remover.place(x=110, y=510)
        bttn_visto=Button(wFavoritos, text="Visto", width=30, height=3)
        bttn_visto.place(x=200, y=510)
        bttn_nvisto=Button(wFavoritos, text="Não Visto", width=30, height=3)
        bttn_nvisto.place(x=290, y=510)

#isto é para filtar os dados da tree mas ainda nao funciona
#copiei do ex11
def dados_treeview():  # Remove TODAS as linhas da Treeview
    tree.delete(*tree.get_children()) 
    tipo = ""
    if vals.get() == True and valf.get() == True:   # Se está checado serie e filme (vals e valf)
        tipo = "T"
    else:
        if vals.get() == True:                      # se está apenas checado vals (serie)
            tipo = "Série\n"
        if valf.get() == True:                      # se está apenas checado valf (filme)
            tipo = "Filme\n"
    f = open(ficheiro, "r", encoding="utf-8")
    lista = f.readlines()
    f.close()
    for linha in lista:
        campos = linha.split(";")
        if tipo == "T" or  campos[2] == tipo:
            if val3.get() == "" or val3.get() == campos[0]:
                    tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3],campos[4], campos[5]))

#remove linha
#selecionas uma linha no catalogo do admin e carregas em remover
def remover(window5):
    selecao=tree.focus()
    selecao=int(selecao[1:])
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
    btnadicionar.place(x=250, y=400)

    btnremover = Button(window5, width = 10, height= 2, text = "Remover", fg="red",command=lambda:remover(window5))
    btnremover.place(x=350, y=400)

    lbladicionar = Label(window5, text="Adicionar novo filme/série")
    lbladicionar.place(x=30, y=220)

    global nome
    nome=StringVar()
    lblnome = Label(window5, text="Nome")
    lblnome.place(x=100, y=250)
    txtnome = Entry(window5, width = 20, textvariable=nome)
    txtnome.place(x=60, y=300)

    global ano
    ano=IntVar()
    lblano = Label(window5, text="Ano")
    lblano.place(x=250, y=250)
    txtano = Entry(window5, width = 20, textvariable=ano)
    txtano.place(x=210, y=300)

    global tipologia
    tipologia=StringVar()
    lbltipologia = Label(window5, text="Tipologia")
    lbltipologia.place(x=370, y=250)
    txttipologia = Entry(window5, width = 20, textvariable=tipologia)
    txttipologia.place(x=350, y=300)

    global categoria
    categoria=StringVar()
    lblcategoria = Label(window5, text="Categoria")
    lblcategoria.place(x=520, y=250)
    txtcategoria = Entry(window5, width = 20, textvariable=categoria)
    txtcategoria.place(x=500, y=300)

    # Panel
    panel1 = PanedWindow(window5, width = 650, height = 200, bd = "3", relief = "sunken")
    panel1.place(x=10, y=10)
    #ListBox
    global tree  
    tree=ttk.Treeview(panel1,height=8,selectmode="browse",columns=("Nome","Ano","Tipologia","Categoria"), show="headings")
    tree.column("Nome", width=180, anchor="c")
    tree.column("Ano", width=150, anchor="c")
    tree.column("Tipologia", width=150, anchor="c")
    tree.column("Categoria", width=150, anchor="c")
    tree.heading("Nome", text="Nome")
    tree.heading("Ano", text="Ano")
    tree.heading("Tipologia", text="Tipologia")
    tree.heading("Categoria", text="Categoria")
    tree.place(x=1, y=1)
    mostrar()
barraMenu()


#foto
ctnCanvas = Canvas(window, width = 350, height = 200, bd = 4, relief = "sunken")
ctnCanvas.place(x=200, y=150)
imginicio = ImageTk.PhotoImage(Image.open("Netflix.jpg"))
ctnCanvas.create_image(180,100, image = imginicio)

lbl = Label(window, text = "Gestor de Filmes", font = ("Helvetica", 12))
lbl.place(x=600, y=250)


window.mainloop()