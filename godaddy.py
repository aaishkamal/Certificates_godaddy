import requests
import json

api_key = "apikey"
secret_key = "secretkey"

headers = {"Authorization" : "sso-key {}:{}".format(api_key, secret_key)}

url = "https://api.godaddy.com/v1/certificates/{certificateId}"

certificate = requests.get(url, headers=headers).json()

data = json.load(certificate)