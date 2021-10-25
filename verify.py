import requests

apiKey = ""

def verify_phone_number(phone_num):
    response = requests.get("https://phonevalidation.abstractapi.com/v1/?api_key="+apiKey+" &phone=14152007986")
    return response.json()["valid"]

if verify_phone_number(+263779525756):
    print("phone is valid")

else:
    print("phone is invalid")
