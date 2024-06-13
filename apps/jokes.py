import requests

def get_new_joke(): 
  url = "https://icanhazdadjoke.com/"
  headers = {"Accept": "application/json"}
  result = requests.get(url, headers=headers)
  joke = result.json()["joke"]
  return joke
