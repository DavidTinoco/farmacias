#-*- coding:utf-8 -*-
import json
with open ("farmacias.json") as data_file:
    data = json.load(data_file)

print "Las farmacias con fax son:"
    
for j in data["directorios"]["directorio"]:
    if len(j["fax"]) > 5:
        print j["nombre"]["content"]
