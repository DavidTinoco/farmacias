#-*- coding:utf-8 -*-
import json
with open ("farmacias.json") as data_file:
    data = json.load(data_file)

for j in data["directorios"]["directorio"]:
    print j
