import requests
data = requests.get("http://192.168.1.231:8080/es2")
data = data.json()

final = 

body = {
	"value" : final
}

a = requests.post("http://192.168.1.231:8080/es2", json = body).json()
print(a["message"])