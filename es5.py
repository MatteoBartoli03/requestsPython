import requests
data = requests.get("http://192.168.1.231:8080/es52")
data = data.json()

final = 

body = {
	"value" : final
}

a = requests.post("http://192.168.1.231:8080/es5", json = body).json()
print(a["message"])