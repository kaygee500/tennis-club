import requests

response = requests.get('http://localhost:8000/api')
print(response.json())