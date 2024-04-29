import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"
# HTTP Requests
get_response = requests.get(
    endpoint, params={"id":1786161155}
)
# print(get_response.text)

# HTTP Requests -> HTMl
# Rest API HTTP Requests -> JSON
# JS objects Nototion -> Python Dict
print(get_response.json())
# print(get_response.status_code)
