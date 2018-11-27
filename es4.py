import requests

req = requests.get("http://192.168.1.231:8080/esercizi/1", headers = {"x-data" : "True"})

data = req.json()

lista = data["data"]

ciao = []

for x in lista:
	if x < 0:
		ciao.append(-x)
	if x >= 0:
		ciao.append(x)

res = requests.post("http://192.168.1.231:8080/esercizi/1", json = {"data" : ciao })

print(res.json())