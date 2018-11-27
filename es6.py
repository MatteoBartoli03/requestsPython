import requests

req = requests.get("http://192.168.1.231:8080/esercizi/3", headers = {"x-data" : "True"})

data = req.json()

lista = data["data"]

ciao = []

media = sum(lista)/len(lista)

for x in lista:
	if x > media:
		ciao.append(x)

print(ciao)

res = requests.post("http://192.168.1.231:8080/esercizi/3", json = {"data" : ciao})

print(res.json())