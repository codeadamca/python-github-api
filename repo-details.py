import os
import mysql.connector
import requests
import datetime

from dotenv import load_dotenv

load_dotenv()

GITHUB_ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')

# print(GITHUB_ACCESS_TOKEN)

url = 'https://api.github.com/repos/BrickMMO/bmos'

headers = {
  'Authorization': 'Bearer ' + GITHUB_ACCESS_TOKEN,
  'Content-Type': 'application/json'
}

response = requests.get(url, headers)
response = response.json()

print('ID: ' + str(response['id']))
print('Full Name: ' + response['full_name'])
print('Owner: ' + response['owner']['login'])
print('URL: ' + response['html_url'])

created_at = datetime.datetime.strptime(response['created_at'], "%Y-%m-%dT%H:%M:%SZ")
updated_at = datetime.datetime.strptime(response['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
pushed_at = datetime.datetime.strptime(response['pushed_at'], "%Y-%m-%dT%H:%M:%SZ")

print('Created At: ' + str(created_at))
print('Updated At: ' + str(updated_at))
print('Pushed At: ' + str(pushed_at))

# print(response)
