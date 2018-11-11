import os, sys
import glob

from tkts.models import Ticket

TKTS_DIR = os.environ.get('TKTS_DIR', '.tkts')

def reported():
    pass 

def get_list():
    files = glob.glob(TKTS_DIR + "/*")
    return [get_issue(f.split('/tkt')[1]) for f in files]


def get_issue(key):
    # if os.exist(filename(key)):
    body = read(key)

    return Ticket(
        id=key,
        summary=body
    )


def create_issue(summary, as_a, would_like, ensure, acceptances, parent=None):
    ticket = Ticket(
        id=ticket_count() + 1,
        summary=summary
    )

    write(ticket)

    return ticket


def comment(issue_id, body):
    pass


def write(ticket):
    path = "{}/{}".format(TKTS_DIR, ticket.id)

    with open(filename(ticket.id), 'w') as fp:
        fp.write(str(ticket))


def read(key):
    # if os.exists(filename(key)):
    with open(filename(key), 'r') as fp:
        return fp.readline()

def ticket_count():
    files = glob.glob(TKTS_DIR + '/*')

    return len(files)


def filename(key):
    return '{}/tkt{}'.format(TKTS_DIR, key)


def init():
    os.mkdir(TKTS_DIR)

# init()
