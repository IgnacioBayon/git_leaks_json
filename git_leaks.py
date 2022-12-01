import re
from sys import exit
from git import Repo
from signal import signal, SIGINT
import json
import pprint

END = "\033[m"

REPO_DIR = "skale/skale-manager"
leaks = ['key', 'password', 'credentials']


def compile_p(leaks):
    compiled_leaks = []
    for leak in leaks:
        compiled_leaks.append(re.compile(leak))
    return compiled_leaks


def extract(url):
    repo = Repo(url)
    return repo


def transform(repo:Repo, compiled_leaks):
    commit_dict = {}
    repo_list = list(repo.iter_commits())
    print(repo.iter_commits())
    for commit in repo_list:
        for leak in compiled_leaks:
            if leak.search(commit.message,re.I):
                commit_dict[commit.hexsha] = commit.message
    return commit_dict


def load(commit_dict): 
    my_commit = {'Commit':commit_dict}
    
    with open('leaks.json', 'w') as fp:
        json.dump(my_commit, fp, indent = 4)

    with open('leaks.json', 'r') as fp:
        data = json.load(fp)

    pp = pprint.PrettyPrinter(indent=4, compact=True)

    print("\n\n\tPretty Printing using pprint module:\n")
    pp.pprint(data)


if __name__ == "__main__":

    compiled_leaks = compile_p(leaks)
    repo = extract(REPO_DIR)
    commit_dict = transform(repo, compiled_leaks)
    load(commit_dict)
    exit(0)