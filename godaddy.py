import requests
import json
import config

api_key = config.api_key
secret_key = config.secret_key

headers = {"Authorization" : "sso-key {}:{}".format(api_key, secret_key)}

url = "https://api.ote-godaddy.com/v1/certificates"

certificate = requests.get(url, headers=headers).json()

data = json.dumps(certificate)

print(data)