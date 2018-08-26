import sys
import json
import requests
import os

def get_repositories(username):
    url = "https://api.github.com/users/" + username + "/repos"
    response = requests.get(url, auth = (os.environ['USER'],os.environ['ACCESS_TOKEN']))
    response_content = json.loads(response.text)

    #listing all pubic repos associated with the username provided
    for repo in response_content:
        print(repo["name"])

if __name__=="__main__":
    username = sys.argv[1]
    get_repositories(username)
