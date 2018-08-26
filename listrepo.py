import sys
import json
import requests
import os

def get_repositories(username,usersaccount, password):
    url = "https://api.github.com/users/" + usersaccount + "/repos"
    response = requests.get(url, auth = (username,password))
    response_content = json.loads(response.text)

    #listing all pubic repos associated with the username provided
    for repo in response_content:
        print(repo["name"])

if __name__=="__main__":
    username = sys.argv[1]
    usersaccount = sys.argv[2]
    password = sys.argv[3]
    get_repositories(username,usersaccount,password)
