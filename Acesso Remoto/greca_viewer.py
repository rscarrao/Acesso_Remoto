from tkinter import *
from tkinter import ttk
import csv
import os
import socket

hostname = []
username = []
combo_lista = []
# busca = input('Nome de quem deseja: ')
texto = []
users = []
cont_user = 0
path = "C://Acesso Remoto"
lista_arquivos = os.listdir(path)
cont_arquvio = 0
cont_linha = 0

with open('Dbdesk.csv', encoding='utf-16') as arquvio:
    texto = csv.reader(arquvio)
    for linha in texto:
            hostname.append(linha)


with open('Dbnote.csv', encoding='utf-16') as arquvio:
    texto = csv.reader(arquvio)
    for linha in texto:
        hostname.append(linha)

documento = hostname[150:301]
del (hostname[150:301])

for lista in hostname:
    try:
        host1 = lista[0]
    except IndexError:
        continue
    combo_lista.append(host1)

for lista2 in documento:
    try:
        host2 = lista2[0]
    except IndexError:
        continue

    combo_lista.append(host2)


def acesso_remoto(**args):
    global cont_arquvio
    global cont_linha
    for i in combo.curselection():
            maquina_l = combo.get(i)
    maquina_n = maquina_l.split(" ", 1)
    maquina = socket.gethostbyname(maquina_n[0])
    for lista in lista_arquivos:
        if "Acesso" in lista:
            pasta = lista_arquivos[cont_arquvio]
            base = os.path.splitext(pasta)[0]
            os.rename(pasta, base + '.txt')
            break
        cont_arquvio += 1

    with open("Acesso.txt", "r+") as arquivo:
        texto = arquivo.readlines()
        for frase in texto:
            if 'host=' in frase:
                texto[cont_linha] = f'host={maquina}\n'
                break
            cont_linha += 1

    with open("Acesso.txt", "w") as arquivo:
        arquivo.writelines(texto)

    for lista in lista_arquivos:
        if "Acesso" in lista:
            lista_arquivos[cont_arquvio] = pasta

    cont_arquvio = 0
    for lista in lista_arquivos:
        if "Acesso" in lista:
            pasta = 'Acesso.txt'
            base = os.path.splitext(pasta)[0]
            os.rename(pasta, base + '.vnc')
            break
        cont_arquvio += 1

    os.startfile("C://Acesso Remoto/Acesso.vnc")
    janela.destroy()
    os.startfile("C://Acesso Remoto/greca_viewer.exe")


def search(event):
    global combo
    value = event.widget.get()
    print(value)

    if value == '':
        data = combo_lista
    else:
        data = []
        for item in combo_lista:
            if value.lower() in item.lower():
                data.append(item)
    Update(data)

def Update(data):
    combo.delete(0, 'end')
    for item in data:
		    combo.insert('end', item)

janela = Tk()
janela.geometry('350x250')
selecao = StringVar()
texto_busca = StringVar()
entry = Entry(janela)
entry.place(x=10, y=60)
entry.bind('<KeyRelease>', search)
label_titulo = Label(janela, text='Acesso remoto')
label_titulo.place(x=10, y=10)
combo = Listbox(janela, width='35')
#combo.get(entry.get)
combo.place(x=10, y=100)
Update(combo_lista)
#combo.bind('<KeyRelease>', search)
botao_acesso = ttk.Button(janela, text='Acessar', command=acesso_remoto)
botao_acesso.place(x=250, y=58)

janela.mainloop()