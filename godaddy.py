import requests
import json

api_key = "3mM44UbC1evZBR_B6j76Te2Z9Dy4r4WJJPXjH"
secret_key = "4t5hA7yFsrswZQC1RrkdFJ"

headers = {"Authorization" : "sso-key {}:{}".format(api_key, secret_key)}

url = "https://api.ote-godaddy.com/v1/certificates"

certificate = requests.get(url, headers=headers).json()

data = json.dumps(certificate)

print(data)