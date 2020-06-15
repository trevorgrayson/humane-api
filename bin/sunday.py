#!/usr/bin/env python3

import os
from json import loads
from http.client import HTTPSConnection

TRELLO_KEY = os.environ['TRELLO_KEY']
TRELLO_TOKEN = os.environ['TRELLO_TOKEN']
ACTIVE = ['pointillism', 'tg@dave', 'Personal']

BOARDS_URL = f"/1/members/me/boards?fields=name,url&key={TRELLO_KEY}&token={TRELLO_TOKEN}"
# LISTS_URL =  f"/1/lists/{}?key={TRELLO_KEY}&token={TRELLO_TOKEN}"
# /cards

if __name__ == '__main__':
    conn = HTTPSConnection('api.trello.com', timeout=2)
    conn.request('GET', BOARDS_URL)

    resp = conn.getresponse()
    projects = []

    if resp.status == 200:
        data = resp.read()
        projects = map(lambda p: (p['name'], p['id']), loads(data))
        # name, id
    else:
        print(resp.status, resp.read())
    conn.close()

    projects = filter(lambda p: p[0] in ACTIVE, projects)

    for project in projects:
        print(project)
