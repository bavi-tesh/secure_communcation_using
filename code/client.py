import requests
from requests.auth import HTTPBasicAuth
import getpass

url = 'https://127.0.0.1:5000/'

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

response = requests.get(url, auth=HTTPBasicAuth(username, password), verify=False)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to connect: {response.status_code}")
