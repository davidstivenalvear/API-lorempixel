#!/user/bin/env phyton3
#autor: david stiven alvear - juan david cano
#programa: API-lorempixel.py
#fecha: sat junio 17 08:00:56 cot 2017
#descripcion: Esta API consulta una base de datos de la pagina lorempixel y estrae las imagenes de acuerdo a los parametros que se le pidan

#esta libreria simplifica el transporte de datos de HTTP
from urllib2 import urlopen

#se declaran las variables del sitio web y los tipos de imagenes
url= "http://lorempixel.com"
tipos = ["abstract","animals","business","cats","city","food","nightlife","fashion","people","nature","sports","technics","transport"]

#el usuario de la API digitaralos valores que desee para la imagen
ancho = raw_input("Cual es el ancho? ")
alto = raw_input("Cual es el alto? ")
tipo = raw_input("Cual es el tipo? ")

#se introduce un ciclo que contiene un rango de (5) imagenes para decargar
for img in range(5):
	url_req= "%s/%s/%s/%s/%d" % (url,ancho,alto,tipos[int(tipo)],img)
	resultado = urlopen(url_req)
	lectura = resultado.read()
	f = open("holder_%d.jpg" % img,"wb")
	f.write(lectura)
	f.close()
