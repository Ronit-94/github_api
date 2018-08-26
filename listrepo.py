import sys
import json
import requests

def get_repositories(username, password):

    url = "https://api.github.com/user/repos"
    r = json.loads(requests.get(url, auth = (username, password)).text)
    for repo in r:
        print(repo["name"])


if __name__=="__main__":
    username = sys.argv[1]
    password = sys.argv[2]


    get_repositories(username, password)
