from github import Github
import sys
import json
import base64
import requests

def get_repositories(username, password):

    url = "https://api.github.com/user/repos"
    #headers = {"Authorization": "Basic " + base64.urlsafe_b64encode("%s:%s" % (username, password)), "Content-type": "application/json"}
    r = json.loads(requests.get(url, auth = (username, password)).text)
    for repo in r:
        print(repo["name"])




if __name__=="__main__":
    username = sys.argv[1]
    password = sys.argv[2]


    get_repositories(username, password)
