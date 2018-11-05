import requests
url = 'https://api.github.com/users/jarota' #my user account
response = requests.get(url)
print(response.json())
