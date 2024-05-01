import requests

endpoint = "http://127.0.0.1:8000/api/product/detail/1/"

get_response = requests.get(
    endpoint, json={"title":"Django","content":"Full Stack Developer","price":"99.99"}
)

print(get_response.json())
