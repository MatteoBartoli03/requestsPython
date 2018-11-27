import requests

ciao = {"nome" : "Matteo Bartoli"}

req = requests.post("http://192.168.1.231:8080/accreditamento", json = ciao)

print(req)