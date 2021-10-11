#!/usr/bin/env python3

import os
from datetime import datetime
from json import loads
from http.client import HTTPSConnection

OUT_FILE = f"{os.environ['HOME']}/velocity"

DOING_COLUMN = 2
DONE_COLUMN = 3
WEEK = 2

TRELLO_KEY = os.environ['TRELLO_KEY']
TRELLO_TOKEN = os.environ['TRELLO_TOKEN']
ACTIVE = ['pointillism', 'tg@dave', 'Personal']

BOARDS_URL = f"/1/members/me/boards?fields=name,url&key={TRELLO_KEY}&token={TRELLO_TOKEN}"
LISTS_URL =  f"/1/boards/%s/lists?key={TRELLO_KEY}&token={TRELLO_TOKEN}"
CARDS_URL =  f"/1/lists/%s/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}"
ARCHIVE_CARDS =  f"/1/lists/%s/archiveAllCards?key={TRELLO_KEY}&token={TRELLO_TOKEN}"

# /cards

if __name__ == '__main__':
    conn = HTTPSConnection('api.trello.com', timeout=2)
    conn.request('GET', BOARDS_URL)

    resp = conn.getresponse()

    def boards():
        boards = []

        if resp.status == 200:
            data = resp.read()
            boards = map(lambda p: (p['name'], p['id']), loads(data))
            # name, id
        else:
            print(resp.status, resp.read())

        boards = filter(lambda p: p[0] in ACTIVE, boards)
        return boards

    def lists():
        lists = []
        for name, id_ in boards():
            conn.request('GET', LISTS_URL % id_)
            resp = conn.getresponse()

            if resp.status == 200:
                data = resp.read()
                all_lists = loads(data)
                # doning = all_lists[DOING_COLUMN]
                dones = all_lists[DONE_COLUMN]
                # week = all_lists[WEEK]
                lists.append({"id": dones['id'], 'project': name})

        return lists

    # cards
    with open(OUT_FILE, 'a') as out:
        now = datetime.now()
        for l in lists():
            conn.request('GET', CARDS_URL % l['id'])
            resp = conn.getresponse()
            if resp.status == 200:
                data = resp.read()
                cards = loads(data)
                line = "\t".join(map(str, (
                    now.strftime('%Y-%m-%d'), l['project'], len(cards)
                )))
                out.write(line + "\n")

                conn.request('POST', ARCHIVE_CARDS % l['id'])
                resp = conn.getresponse()
                resp.read()
