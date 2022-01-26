from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x500")
window.title("Test")

nome_selecao = "Nome(0)"
#txt_comentario = "text text text"
username = "user123"
spin = 6

button = Button(window,height=3, width=10, text=">", command = lambda: avaliar(spin,nome_selecao))
button.place(x=20, y=20)

def add_favoritos(nome_selecao,selecao):
    with open("favoritos.txt", "r", encoding="UTF-8") as f:
        lista = f.readlines()
        all_users = []
        for line in lista:
            campos = line.split(";")
            all_users.append(campos[0])
            if username == campos[0]:
                break
        if (username not in all_users)==True:
            msg = messagebox.showwarning("Sessão não iniciada", "Por favor faça login!")
        for i in range(1,len(campos)):
            if campos[i] == nome_selecao:
                msg = messagebox.showwarning("Já adicionado!", "Já foi adicionado à sua lista!")
                break
            else:
                lista[lista.index(line)] = line[0:len(line)-2] + ";" + nome_selecao +"\n"
                favoritos = open("favoritos.txt", "w")
                favoritos.write("")
                favoritos = open("favoritos.txt", "a", encoding="UTF-8")
                for i in range(len(lista)):
                    favoritos.write(str(lista[i]))  #volta a colocar toda a informacao no ficheiro com a adicao do novo comentario
                break



        for line in lista:
            if username==campos[0]:
                filme=nome_selecao
                lista2=campos[1]
                for line in lista2:
                    seccao=lista2.split("+")
                    if (filme not in seccao)==True:
                        with open("sample.txt", "a") as objeto:
                            objeto.write(filme+"+")
                    else:
                        msg = messagebox.showwarning("Já adicionado!", "Já foi adicionado à sua lista!")

#-------------
                pos = all_comments.index(line)
                all_comments[pos] = str(line[0:len(line)-2] + ";" + username + ": " + txt_comentario)  #muda o elemento da lista(linha com todos os comentarios de um determinado filme/serie)
                comentarios = open("comentarios.txt", "w")
                comentarios.write("")     #apaga todo o ficheiro
                comentarios = open("comentarios.txt", "a", encoding="UTF-8")
                for i in range(len(all_comments)):
                    comentarios.write(str(all_comments[i]))  #volta a colocar toda a informacao no ficheiro com a adicao do novo comentario
                break

window.mainloop()