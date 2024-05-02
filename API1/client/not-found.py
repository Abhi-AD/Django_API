import requests

endpoint = "http://127.0.0.1:8000/api/product/detail/1852845451451451/"

get_response = requests.get(
    endpoint)

print(get_response.json())
