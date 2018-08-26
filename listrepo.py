import sys
import json
import requests

token = "6fe21b93e82a0cca4e555689c872cca6fbd6f014"
user = "Ronit-94"

def get_repositories(username):
    url = "https://api.github.com/users/" + username + "/repos"
    response = requests.get(url, auth = (user, token))
    response_content = json.loads(response.text)

    #listing all pubic repos associated with the username provided
    for repo in r:
        print(repo["name"])


if __name__=="__main__":
    username = sys.argv[1]

    get_repositories(username)
