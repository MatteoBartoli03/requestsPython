import requests

req = requests.get(
	"http://192.168.1.231:8080/esercizi/*", #al posto di * inserisci numero esercizio
	headers = {"x-data" : "True"}# controlla che la consegna sia la stessa
)

data = req.json()

print(data) #per stampare il json con la consegna e se abbiamo messo gli eaders giusti anche la lista di dati

lista = data["data"]
final = []

#procedimento

res = requests.post(
	"http://192.168.1.231:8080/esercizi/*",  #al posto di * inserisci numero esercizio
	json = {"data" : final } #se il file da passare è un json e la chiave di esso dev'essere data
)

print(res.json()) # stampare la risposta finale 