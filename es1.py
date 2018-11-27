import requests
data = requests.get("http://192.168.1.231:8080/es1")
data = data.json()

s = sum(data["data"])

final = s/len(data["data"])

body = {
	"value" : final
}

a = requests.post("http://192.168.1.231:8080/es1", json = body).json()
print(a["message"])