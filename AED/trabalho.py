#Beatriz Rodrigues, nº aluno:
#Daniela Moreira, nº aluno: 40210349
#Daniela Monteiro, nº aluno: 40210288
from tkinter import *

window = Tk()
window.geometry("1000x700")
window.title('Gestor de filmes e séries')

#login
data = "userdata.txt"

login = Button(window, text="Iniciar sessão", fg='blue', width = 20)
login.place(x=10, y=10)

#sidebar
sidebar = Menu(window)
#filmes
filmes = Menu(sidebar)
filmes.add_command(label="Nome de filme", command="noaction")
sidebar.add_cascade(label="Filmes", menu = sidebar)
#series
series = Menu(sidebar)
series.add_command(label="Nome de série", command="noaction")
sidebar.add_cascade(label="Séries", menu = sidebar)
#categorias
categories = Menu(sidebar)
categories.add_command(label="categoria", command="noaction")
sidebar.add_cascade(label="Categorias", menu = sidebar)
#Top rated
toprated = Menu(sidebar)
toprated.add_command(label="Nome", command="noaction")
sidebar.add_cascade(label="Top rated", menu = sidebar)

window.configure(menu=sidebar)

window.mainloop()