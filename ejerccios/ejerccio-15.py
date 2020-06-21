

"""

Remplazar cada letra de una frase dada por el usuario por 
la posición que le corresponde en el abecedario y mostrar
 el nuevo string en pantalla. (Los espacios no se remplazan) .

  Ejemplo: frase : 'Hola' salida : 815121 H(8) o(15) l(12) a(1)
"""



def reempla_frase(frases):
	vocales = {
			'a':1,'b':2,'c':3,'d':4,'e':5,
			'f':6,'g':7,'h':8,
			'i':9,'j':10,'k':11,
			'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
			'r':18,'s':19,'t':20,
			'u':21,'v':22,'w':23,
			'x':24,'y':25,'z':26
		}
	for vocal, posicion in vocales.items():
		for i in frases:
			if vocal in i:
				a = i,f"({posicion})"
				print(a)

def main():
	frases = input("ingresar una frase:")
	resultado = reempla_frase(frases)
	print(frases,resultado)



if __name__ == '__main__':
	main()