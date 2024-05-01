import requests

endpoint = "http://127.0.0.1:8000/api/product/create/"

data={"title":"Django","content":"Full Stack Developer","price":99.99}

get_response = requests.post(
    endpoint,json=data
)

print(get_response.json())
