#-*- coding:utf-8 -*-
import json
with open ("farmacias.json") as data_file:
    data = json.load(data_file)

#1

print "Las farmacias con fax son:"
    
for j in data["directorios"]["directorio"]:
    if len(j["fax"]) > 5:
        print j["nombre"]["content"]

pausa = raw_input("Pulse cualquier tecla para continuar con la ejecución del programa")

#2 
verano = 0
for j in data["directorios"]["directorio"]:
    temp = j.get("horario")
    if len(temp) > 10:
        if temp.find("Verano") != -1:
            verano = verano + 1
print "Hay " + str(verano) + " farmacias con un horario especial en verano."
    

#3

calle = raw_input("Introduzca la calle a buscar (C/,Avda.,Plaza): ")
existe = False 
for j in data["directorios"]["directorio"]:
    if j["direccion"][0].startswith(calle):
        existe = True
        numero = j["direccion"][0]
        print "En dicha calle se encuentra una farmacia en el número" + str(numero).split(",")[1]
if not existe:
    print "No hay ninguna farmacia en dicha calle"        


#4

farmacia = raw_input("Introduzca el nombre de la farmacia para conocer su horario: ")

existe = False
for j in data["directorios"]["directorio"]:
    if j["nombre"]["content"].startswith(farmacia):
        existe = True
        horario = j.get("horario")
        print "El horario de dicha farmacia es: " + horario
        
if not existe:
    print "No hay ninguna farmacia con dicho nombre"

#5

farmacia = raw_input("Introduzca el nombre de la farmacia para conocer localización en el mapa: ")

existe = False
for j in data["directorios"]["directorio"]:
    if j["nombre"]["content"].startswith(farmacia):
        existe = True
        latitud = j["localizacion"]["content"].split(" ")[0][:6]
        longitu = j["localizacion"]["content"].split(" ")[1][:5]
        print "La localización en un mapa, de dicha farmacia, es:\n http://openstreetmap.org/#map=17/" + str(latitud) + "/" + str(longitu)
        
if not existe:
    print "No hay ninguna farmacia con dicho nombre"
