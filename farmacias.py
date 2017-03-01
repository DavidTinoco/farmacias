#-*- coding:utf-8 -*-
import json
with open ("farmacias.json") as data_file:
    data = json.load(data_file)

#1

print "Las farmacias con fax son:"
    
for j in data["directorios"]["directorio"]:
    if len(j["fax"]) > 5:
        print j["nombre"]["content"]

#2 


#3

calle = raw_input("Introduzca la calle a buscar (C/,Avda.,Plaza): ")
existe = False 
for j in data["directorios"]["directorio"]:
    if j["direccion"][0].startswith(calle):
        existe = True
        numero = j["direccion"][0]
        print "En dicha calle se encuentra una farmacia en el número" + str(numero).split(",")[1]
if not existe:
    print "No hay ninguna farmacia en dich calle"        


#4

farmacia = raw_input("Introduzca el nombre de la farmacia: ")
