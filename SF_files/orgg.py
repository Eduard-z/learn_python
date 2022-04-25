import requests

params_post = {
    "grant_type": "password",
    "client_id": "YjkyMzJmNDUzMGNmOTYzODVlNDQ0ZjE2OTUxOTU1NDI5MGViN2I3NWU3YTFjNmY300D6F000002JvCk",
    "client_secret": "3490590311975058371",
    "username": "ed@ed.ed",
    "password": "Cheglad3e|"
                }

req_post = requests.post(
    "https://login.salesforce.com/services/oauth2/token", params=params_post)
# query = "SELECT Name From Account WHERE ShippingCity='San Francisco' OR ShippingCity='New York'"
params_get = {
    "q": "SELECT Name From Account WHERE ShippingCity='San Francisco' OR ShippingCity='New York'"}
# token = "Bearer " + req_post.json()["access_token"]
headers_get = {"Authorization": "Bearer " + req_post.json()["access_token"],
               "Content-Type": "application/json"
               }
req_get = requests.get("https://ap4.salesforce.com/services/data/v43.0/query",
                       headers=headers_get, params=params_get)
print(req_get.json())
input("Press any key")
