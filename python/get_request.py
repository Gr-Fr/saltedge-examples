from saltedge import SaltEdge

app = SaltEdge("client-id", "service-secret", "private.pem")

url = "https://www.saltedge.com/api/v5/countries"
response = app.get(url)
data = response.json()
print(data)
