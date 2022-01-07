#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Antonio Villanueva Segura 
Una pequena ayuda para resolver paraulogic 
https://paraulogic.rodamots.cat/
"""

def limpiar_acentos(text):
	""" elimina acentos de un string """
	acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A','E': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
	for acen in acentos:
		if acen in text:
			text = text.replace(acen, acentos[acen])
	return text
		
def testLinea ( letras,obligatoria,linea):
	""" mira si una palabra del diccionario contiene algunas  letras minimo 3 """

	#print (letras,"con ",limpiar_acentos(linea), "longitud linea ",len (linea))
	contiene =0 #contador de ocurrencias 
	
	#Recorre las letras de una palabra en el diccionario 
	for letraEnLinea in limpiar_acentos (linea.split("/")[0]):
		if ( (letraEnLinea in letras) or (obligatoria== letraEnLinea)):
			contiene +=1 #ha encontrado una ocurrencia
	
	#Si la palabra contiene minimo 3 ocurrencias es aceptada	
	if ( (contiene >=3)   and ( len(linea)== contiene)   ) :	
		return True			
	return False

def verConjunto(conjunto):
	""" ver elementos no repetidos en el conjunto set """
	for elemento in conjunto:
		print (elemento.strip(),end=" , ")

if __name__ == "__main__":

	letras = input ("Introduce las letras ")
	especial =input ("Introduce la letra central obligatoria ")
	resultado={""}

	#letras="anodrg"
	#especial="f"

	#with open("catalaBig.dic", encoding="latin-1") as fname:
	with open("catalaBig.dic") as fname:
		# recorre las palabras del diccionario por lineas
		for linea in fname:
		
			if testLinea(letras.strip(),especial,linea.strip()):		

				if especial  in linea:
					#print (linea)
					resultado.add(linea)
					
	verConjunto(resultado)
