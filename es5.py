import requests

req = requests.get("http://192.168.1.231:8080/esercizi/2", headers = {"x-data" : "True"})

data = req.json()

lista = data["data"]

ciao = []

for x in lista:
	ciao.append(x[0])

print(ciao)

res = requests.post("http://192.168.1.231:8080/esercizi/2", json = {"data" : ciao})

print(res.json())