import requests

headers = {'Authorization': 'Bearer e22483e33282ed2f16cbfeb975db16d65e13dea5'}

endpoint = "http://127.0.0.1:8000/api/product/create/"
# http://127.0.0.1:8000/admin/

data={"title":"Django","content":"Full Stack Developer","price":99.99}

get_response = requests.post(
    endpoint,json=data, headers=headers
)

print(get_response.json())
