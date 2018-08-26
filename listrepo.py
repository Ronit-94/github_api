from github import Github
import sys

def get_repositories(username, password):
    g = Github(username, password)

    for repo in g.get_user().get_repos():
        print(repo.name)

if __name__=="__main__":
    username = sys.argv[1]
    password = sys.argv[2]


    get_repositories(username, password)
