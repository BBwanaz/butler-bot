import requests

parameter = {'country' : "Zimbabwe"}
response = requests.get("https://coronavirus-tracker-api.herokuapp.com/v2/locations?source=jhu", params = parameter).json()


print(response)

