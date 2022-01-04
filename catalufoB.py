

def testLinea ( letras,linea):
	#print (letras , " con ",linea)
	
	for letraEnLinea in linea.split("/")[0]:
		if letraEnLinea not in letras:
			return False
	return True

if __name__ == "__main__":

	#letras = input ("Introduce letras ")
	#especial =input ("letra obligatoria")

	letras="xauisdb"
	especial="a"
	""" unicode(str, errors='ignore') """
	with open("catala.dic", encoding="latin-1") as fname:
		""" lee lineas"""
		for linea in fname:
			
			if testLinea(letras.strip(),linea.strip()):
				if especial  in linea:
					print(linea.split("/")[0])
				

	

