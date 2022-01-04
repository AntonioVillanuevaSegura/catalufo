"""
Antonio Villanueva Segura 
"""


def limpiar_acentos(text):
	""" elimina acentos de un string """
	acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'E': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
	for acen in acentos:
		if acen in text:
			text = text.replace(acen, acentos[acen])
	return text
	

	
def testLineaB ( letras,obligatoria,linea):
	""" mira si una palabra del diccionario contiene algunas  letras minimo 3 """

	#print (letras,"con ",limpiar_acentos(linea), "longitud linea ",len (linea))
	contiene =0 #contador de ocurrencias 
	
	#Recorre las letras de una palabra en el diccionario 
	for letraEnLinea in limpiar_acentos (linea.split("/")[0]):
		if ( (letraEnLinea in letras) or (obligatoria== letraEnLinea)):
			contiene +=1 #ha encontrado una ocurrencia
		
	if ( (contiene >=3)   and ( len(linea)== contiene)   ) :	
		return True
			

	return False
	

if __name__ == "__main__":

	letras = input ("Introduce las letras ")
	especial =input ("Introduce la letra obligatoria ")

	#letras="roeign"
	#obligatoria="d"
	""" unicode(str, errors='ignore') """
	with open("catala.dic", encoding="latin-1") as fname:
		print ("Diccionario abierto ")
		""" lee lineas"""
		for linea in fname:
			
			#if testLinea(letras.strip(),linea.strip()):
			if testLineaB(letras.strip(),obligatoria,linea.split("/")[0]):		
	
				if obligatoria  in linea:
					print(linea.split("/")[0])
				

	
