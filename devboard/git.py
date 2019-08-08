import os
import http.client

# oauth ?client_id=xxxx&client_secret=yyyy'

GITHUB_HOST = 'api.github.com'
USERNAME='rs-trevor'

conn = http.client.HTTPSConnection(GITHUB_HOST)

def all_repos(): 
    '/orgs/octokit/repos'


def repo_details(): '/repos/octokit/octokit.rb'

def headers():
    return {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': 'token XYZ'
    }

def status():
    """ Interface Method """
    status = {}

    for repo in repos():
        status[repo] = pr_status(repo)

    return status

def repos():
    with open(os.environ['HOME'] + '/.gitrepos') as repos:
        for repo in repos:
            yield repo.strip()


def pr_status(repo):
    url = f"/v3/repos/{repo}"  # .rb
    conn.request('GET', url)
    res = conn.getresponse()
    data = res.read()
    
    print(data)
    return {}

print(status())
