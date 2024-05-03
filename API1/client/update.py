import requests

endpoint = "http://127.0.0.1:8000/api/product/update/1/"
data={
    "title":"Python Langauges For Programming Langauges",
    "price":800
}

get_response = requests.put(
    endpoint, json=data
)

print(get_response.json())
