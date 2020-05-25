from saltedge import SaltEdge
import json

app = SaltEdge("client-id", "service-secret", "./private.pem")

url = "https://www.saltedge.com/api/v5/logins/1234/refresh"
payload = json.dumps({"data": {"fetch_type": "recent"}})
response = app.put(url, payload)
data = response.json()
print(data)
