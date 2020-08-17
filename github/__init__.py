from os import environ
from json import loads
import logging
from http.client import HTTPSConnection

# logging.basicConfig()

TOKEN = environ['USER_GIT_TOKEN']

conn = HTTPSConnection('api.github.com')

headers = { 
    "Authorization": f"token {TOKEN}",
    "User-Agent": "trevorgrayson",
    "Accept": "application/json"
}


def issues():
    url = '/issues?filter=created&state=open'

    conn.request("GET", url, headers=headers)
    resp = conn.getresponse()

    issues = loads(resp.read().decode('utf-8'))

    status_url = issues[0]['repository']['statuses_url']
    conn.request("GET", status_url, headers=headers)
    status_resp = conn.getresponse()
    print(status_resp.read().decode('utf-8'))

    logging.info(f'{url}: {resp.status}')
    if resp.status == 200:
        return issues
