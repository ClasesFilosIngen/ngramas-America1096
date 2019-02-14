import operator

def Ngrama(n, palabra, archivo):
	lista = []
	for x in range(len(palabra)-(n-1)):
		lista.append(palabra[x:x+n])	#Manda a una lista los ngramas

	dic = {}
	for w in lista:
		if ' ' in w or '\n' in w:
			pass
		else:
			dic.update({w : lista.count(w)}) #Se agrega en un diccionario el ngrama y se actualiza el numero de apariciones

	l = sorted(dic.items(), key=operator.itemgetter(1)) #Se acomoda de menor al mayor numero de apariciones en una lista
	l.reverse() #Se invierte la lista para que sea de mayor a menor el numero de apariciones
	return (l)

def mostrarNgramas(ngramas):
	num = int(input("\nCuantos ngramas desea ver? "))
	if num > len(ngramas):	print(ngramas) #Si el numero de ngramas que se desea ver es mayor al numero de ngramas se muestran todos
	else:
		for x in range(num): #Se muestra el numero de ngramas indicados
			print(ngramas[x]) 
	
def main():
	arch = open('ngramas.txt','w+')
	opc = input("\nDesea ingresar texto?\n1)Desde teclado\n2)Desde archivo\n3)Archivos dados\n$$")
	n = int(input("\nIngrese n: $$"))
	if opc == "1":
		texto = input("\nIngrese texto:\n$$")
		mostrarNgramas(acomodarNgrama(n, texto, arch))
	elif opc == "2":
		doc = input("\nIngrese nombre del archivo(Ej:archivo.txt):\n$$")
		d = open(doc, 'r')
		texto = d.read()	
		mostrarNgramas(acomodarNgrama(n, texto, arch))
		d.close()
	elif opc == "3":
		esp = open('esp.txt', 'r')
		#ing = open('ing.txt', 'r')
		#frances = open('frances.txt', 'r')
		texto1 = esp.read()	
		#texto2 = ing.read()	
		#texto3 = frances.read()	
		print("\n\n\tTexto en español")
		mostrarNgramas(Ngrama(n, texto1, arch))
		#print("\n\n\tTexto en ingles")
		#mostrarNgramas(Ngrama(texto2, arch))
		#print("\n\n\tTexto en frances")
		#mostrarNgramas(Ngrama(texto3, arch))
		esp.close()
		#ing.close()
		#frances.close()
	else:
		main()
	arch.close()

main()