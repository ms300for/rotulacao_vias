from tkinter import *
import os
from PIL import Image, ImageTk
import shutil

path = os.getcwd()
path2 = path + "\\imagens\\"
arquivos = os.listdir(path)
path3 = None

def init_pastas():

	root.frame1 = Frame()
	root.frame1.pack()

	root.mensagem1 = Label(root.frame1, text = "Insira o nome da pasta")
	root.mensagem1.pack()

	root.pasta1 = Entry(root.frame1)
	root.pasta1.pack(side = LEFT)

	pasta1 = root.pasta1.get()

	root.botao1 = Button(root.frame1)
	root.botao1["text"] = "ok"
	root.botao1["command"] = lambda: obter_pasta_1()
	root.botao1.pack()
	return

def obter_pasta_1():
	pasta_imagem = root.pasta1.get()
	if pasta_imagem not in arquivos:
		root.frame1.destroy()
		mensagem_erro("erro_1")
	else:
		root.frame1.destroy()
		global path3
		path3 = pasta_imagem
		rotulacao()


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
		root2.botao2["command"] = lambda: [init_pastas(), root2.destroy()]
		root2.botao2.pack()

def rotulacao(lista_imagens = None):
	if lista_imagens == None:
		lista_imagens = os.listdir(path+"\\"+path3)
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

	image = Image.open(path+"\\"+path3+"\\"+lista_imagens[0])
	image = image.resize((854,480))
	photo = ImageTk.PhotoImage(image)

	root.imagem1 = Label(root.frame3, text = "adicionando", image = photo)
	root.imagem1.image = photo
	root.imagem1.pack()

	root.mensagem3 = Label(root.frame3, text = "Deseja rotular essa imagem?")
	root.mensagem3.pack()

	root.botao1 = Button(root.frame3)
	root.botao1["text"] = "Sim"
	root.botao1["command"] = lambda: classificar_vegetacao(lista_imagens[0], lista_imagens)
	root.botao1["width"] = 50
	root.botao1.pack(side=LEFT)

	root.botao2 = Button(root.frame3)
	root.botao2["text"] = "Não"
	root.botao2["command"] = lambda: remover(lista_imagens[0], lista_imagens)
	root.botao2["width"] = 50
	root.botao2.pack(side=RIGHT)

def classificar_vegetacao(imagem, lista_imagens):
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
	root.botao1["text"] = "Ruim"
	root.botao1["command"] = lambda: classificar_sinalizacao(0, imagem, lista_imagens)
	root.botao1.pack(side=LEFT)

	root.botao2 = Button(root.frame2)
	root.botao2["text"] = "Regular"
	root.botao2["command"] = lambda: classificar_sinalizacao(1, imagem, lista_imagens)
	root.botao2.pack(side=LEFT)

	root.botao3 = Button(root.frame2)
	root.botao3["text"] = "Bom"
	root.botao3["command"] = lambda: classificar_sinalizacao(2, imagem, lista_imagens)
	root.botao3.pack(side=LEFT)

def classificar_sinalizacao(vegetacao,imagem, lista_imagens):
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
	classificacao = []
	classificacao.append(vegetacao)
	
	root.frame2.destroy()

	root.frame2 = Frame()
	root.frame2.pack()
	
	root.sinalizacao1 = Label(root.frame2, text = "Classifique a sinalização")
	root.sinalizacao1.pack()

	root.botao1 = Button(root.frame2)
	root.botao1["text"] = "Ruim"
	root.botao1["command"] = lambda: classificar_drenagem(classificacao, 0, imagem, lista_imagens)
	root.botao1.pack(side=LEFT)

	root.botao2 = Button(root.frame2)
	root.botao2["text"] = "Regular"
	root.botao2["command"] = lambda: classificar_drenagem(classificacao, 1, imagem, lista_imagens)
	root.botao2.pack(side=LEFT)

	root.botao3 = Button(root.frame2)
	root.botao3["text"] = "Bom"
	root.botao3["command"] = lambda: classificar_drenagem(classificacao, 2, imagem, lista_imagens)
	root.botao3.pack(side=LEFT)

def classificar_drenagem(classif, sinalizacao, imagem, lista_imagens):
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
	classificacao = classif
	classificacao.append(sinalizacao)
	root.frame2.destroy()

	root.frame2 = Frame()
	root.frame2.pack()
	
	root.drenagem1 = Label(root.frame2, text = "Classifique a drenagem")
	root.drenagem1.pack()

	root.botao1 = Button(root.frame2)
	root.botao1["text"] = "Ruim"
	root.botao1["command"] = lambda: placas(classificacao, 0, imagem, lista_imagens)
	root.botao1.pack(side=LEFT)

	root.botao2 = Button(root.frame2)
	root.botao2["text"] = "Regular"
	root.botao2["command"] = lambda: placas(classificacao, 1, imagem, lista_imagens)
	root.botao2.pack(side=LEFT)

	root.botao3 = Button(root.frame2)
	root.botao3["text"] = "Bom"
	root.botao3["command"] = lambda: placas(classificacao, 2, imagem, lista_imagens)
	root.botao3.pack(side=LEFT)

	root.botao4 = Button(root.frame2)
	root.botao4["text"] = "Bom (não existente)"
	root.botao4["command"] = lambda: placas(classificacao, 3, imagem, lista_imagens)
	root.botao4.pack(side=LEFT)

def placas(classif, drenagem, imagem, lista_imagens):
	classificacao = classif
	classificacao.append(drenagem)
	root.frame2.destroy()

	root.frame2 = Frame()
	root.frame2.pack()
	
	root.vegetacao1 = Label(root.frame2, text = "Existe sinalização vertical?")
	root.vegetacao1.pack()

	root.botao1 = Button(root.frame2)
	root.botao1["text"] = "Sim"
	root.botao1["command"] = lambda: salvar_dados(classificacao, 1, imagem, lista_imagens)
	root.botao1.pack(side=LEFT)

	root.botao2 = Button(root.frame2)
	root.botao2["text"] = "Não"
	root.botao2["command"] = lambda: salvar_dados(classificacao, 0, imagem, lista_imagens)
	root.botao2.pack(side=LEFT)

def salvar_dados(classif, placas, imagem, lista_imagens):
	classificacao = classif
	classificacao.append(placas)
	root.frame2.destroy()
	texto = imagem
	for i in classificacao:
		texto += ","
		texto += str(i)
	texto = texto + "\n"
	arquivo = open("dados.csv", "a")
	arquivo.write(texto)
	arquivo.close()

	shutil.move(path+"\\"+path3+"\\"+imagem, path2+imagem)
	lista_imagens.remove(imagem)
	root.frame3.destroy()
	rotulacao(lista_imagens)



def remover(imagem, lista_imagens):
	lista_imagens.remove(imagem)
	root.frame3.destroy()
	rotulacao(lista_imagens)
def inicio():
	if "dados.csv" not in arquivos:
		arquivo = open("dados.csv", "w")
		arquivo.close()
	else:
		pass

	if "imagens" not in arquivos:
		os.mkdir(path+"\\imagens")
	else:
		pass

	init_pastas()



root = Tk()
root.title("Rotulação da via lateral")
root.geometry("640x400")
root.configure(background = "#dde")
inicio()
root.mainloop()
