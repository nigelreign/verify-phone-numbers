import requests

# https://app.abstractapi.com/api/phone-validation/tester

apiKey = ""
response = requests.get("https://phonevalidation.abstractapi.com/v1/?api_key="+apiKey+" &phone=14152007986")
print(response.status_code)
print(response.content)
