import requests

headers = {"Authorization": "Token 3cd347d7f41d0c17e2b9f544750f67ff415316ca"}
response = requests.get("http://127.0.0.1:8000/datalist/", headers=headers)
noAuthenResponse = requests.get("http://127.0.0.1:8000/jobflow/")


print(response.json())
