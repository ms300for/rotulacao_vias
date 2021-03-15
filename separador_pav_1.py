import os
import shutil

from tkinter import *
from PIL import Image, ImageTk

path = os.getcwd()
path2 = None

def verificacao_pastas(path, path2):

	defeitos = ["Buraco", "Remendo", "Trinca", "Multidefeitos", "Limpa", "Outros"]
	lista_1 = os.listdir(path)

	if "imagens_separadas" not in lista_1:
		os.makedirs(path+"\\imagens_separadas")

	arquivos = os.listdir(path+"\\imagens_separadas")

	if (path2) not in arquivos:
		os.makedirs(path + "\\" + "imagens_separadas\\" + path2)

	pasta_defeitos = path + "\\" + "imagens_separadas\\" + path2
	pastas = os.listdir(pasta_defeitos)

	for defeito in defeitos:
		if defeito not in pastas:
			os.makedirs(path + "\\" + "imagens_separadas\\" + path2 + "\\" + defeito)


def funcao_pass():
	pass

def mensagem_erro(erro):
	root2 = Tk()
	if erro == "erro_1":
		texto1 = "Erro 001: pasta não encontrada."

		root2.frame2 = Frame(root2)
		root2.frame2.pack()

		root2.mensagem2 = Label(root2.frame2, text = texto1)
		root2.mensagem2.pack()

		root2.botao2 = Button(root2.frame2)
		root2.botao2["text"] = "ok"
		root2.botao2["command"] = lambda: [root2.destroy()]
		root2.botao2.pack()




def inicio():
	root.path = os.getcwd()
	root.frame1 = Frame(master)
	root.frame1.pack()

def abrir_pasta():
	root.frame1 = Frame()
	root.frame1.pack()

	root.mensagem1 = Label(root.frame1, text = "Insira o nome da pasta")
	root.mensagem1.pack()

	root.entrada_pasta = Entry(root.frame1)
	root.entrada_pasta.pack(side = LEFT)


	root.botao1 = Button(root.frame1)
	root.botao1["text"] = "ok"
	root.botao1["command"] = lambda: verificar_pasta()
	root.botao1.pack()

def verificar_pasta():
	global path
	global path2
	path2 = root.entrada_pasta.get()
	arquivos = os.listdir()
	if path2 not in arquivos:
		root.frame1.destroy()
		mensagem_erro("erro_1")
	else:
		verificacao_pastas(path, path2)
		root.frame1.destroy()
		rotulacao()

def rotulacao(lista_imagens = None):
	global path
	global path2

	if lista_imagens == None:
		lista_imagens = os.listdir(path+"\\"+path2)
	if len(lista_imagens) >= 1:
		mostrar_img(lista_imagens)
	else:
		root.frame1 = Frame()
		root.frame1.pack()

		root.mensagem1 = Label(root.frame1, text = "Pasta vazia")
		root.mensagem1.pack()

		root.botao1 = Button(root.frame1)
		root.botao1["text"] = "finalizar"
		root.botao1["command"] = lambda: root.quit()
		root.botao1.pack()

def mostrar_img(lista_imagens):
	root.frame3 = Frame()
	root.frame3.pack()

	image = Image.open(path+"\\"+path2+"\\"+lista_imagens[0])
	image = image.resize((854,480))
	photo = ImageTk.PhotoImage(image)

	root.imagem1 = Label(root.frame3, text = "adicionando", image = photo)
	root.imagem1.image = photo
	root.imagem1.pack()

	root.mensagem3 = Label(root.frame3, text = "Deseja rotular essa imagem?")
	root.mensagem3.pack()

	root.botao1 = Button(root.frame3)
	root.botao1["text"] = "Sim"
	root.botao1["command"] = lambda: classificar_imagem(lista_imagens[0], lista_imagens)
	root.botao1["width"] = 50
	root.botao1.pack(side=LEFT)

	root.botao2 = Button(root.frame3)
	root.botao2["text"] = "Não"
	root.botao2["command"] = lambda: remover(lista_imagens[0], lista_imagens)
	root.botao2["width"] = 50
	root.botao2.pack(side=RIGHT)

def classificar_imagem(imagem, lista_imagens):
	"""
	classificações
	0 - ruim
	1 - regular
	2 - bom
	3 - bom(não presente): válido apenas para drenagem

	0 - inexistência de placas
	1 - existência de placas

	classificação da vegetação
	classificação da sinalização
	classificação da drenagem
	existencia de placas
	"""
	root.mensagem3.destroy()
	root.botao1.destroy()
	root.botao2.destroy()

	root.frame2 = Frame()
	root.frame2.pack()
	
	root.vegetacao1 = Label(root.frame2, text = "Classifique a vegetacao")
	root.vegetacao1.pack()

	root.botao1 = Button(root.frame2)
	root.botao1["text"] = "Buraco(s)"
	root.botao1["command"] = lambda: mover_imagem(0, imagem, lista_imagens)
	root.botao1.pack(side=LEFT)

	root.botao2 = Button(root.frame2)
	root.botao2["text"] = "Remendo(s)"
	root.botao2["command"] = lambda: mover_imagem(1, imagem, lista_imagens)
	root.botao2.pack(side=LEFT)

	root.botao3 = Button(root.frame2)
	root.botao3["text"] = "Trinca(s)"
	root.botao3["command"] = lambda: mover_imagem(2, imagem, lista_imagens)
	root.botao3.pack(side=LEFT)

	root.botao4 = Button(root.frame2)
	root.botao4["text"] = "Limpa"
	root.botao4["command"] = lambda: mover_imagem(3, imagem, lista_imagens)
	root.botao4.pack(side=LEFT)

	root.botao5 = Button(root.frame2)
	root.botao5["text"] = "Multidefeitos"
	root.botao5["command"] = lambda: mover_imagem(4, imagem, lista_imagens)
	root.botao5.pack(side=LEFT)

	root.botao6 = Button(root.frame2)
	root.botao6["text"] = "Outro(s)"
	root.botao6["command"] = lambda: mover_imagem(5, imagem, lista_imagens)
	root.botao6.pack(side=LEFT)

def mover_imagem(valor, imagem, lista_imagens):
	root.frame2.destroy()
	defeitos = ["Buraco", "Remendo", "Trinca", "Limpa", "Multidefeitos", "Outros"]
	global path
	global path2
	shutil.move(path+"\\"+path2+"\\"+imagem, path+"\\"+"imagens_separadas"+"\\"+path2
		+"\\"+defeitos[valor]+"\\"+imagem)

	lista_imagens.remove(imagem)
	root.frame3.destroy()
	rotulacao(lista_imagens)

def remover(imagem, lista_imagens):
	lista_imagens.remove(imagem)
	root.frame3.destroy()
	rotulacao(lista_imagens)

root = Tk()
root.title("Separador_pavimentos_alpha 0.1")
root.geometry("800x640")

Barra_Menu = Menu(root)

menu_iniciar = Menu(Barra_Menu, tearoff = 0)
menu_iniciar.add_command(label = "Abrir pasta", command = lambda: abrir_pasta())

Barra_Menu.add_cascade(label = "Rotulação", menu =menu_iniciar)

root.config(menu = Barra_Menu)

root.mainloop()