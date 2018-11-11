import os
import jira
import tkts

HOST = os.environ.get('HAPI_TKTS')

SERVICE = tkts

if HOST != '.':
    SERVICE = jira


def reported():
    SERVICE.reported()

def get_list():
    tickets = SERVICE.get_list()

    if tickets:
        for ticket in tickets:
            print ticket

def get_issue(key):
    ticket = SERVICE.get_issue(key)
    print ticket

def comment(issue_id, body):
    SERVICE.comment(issue_id, body)

def create_issue(summary, as_a, would_like, ensure, acceptances, parent=None):
    ticket = SERVICE.create_issue(summary, as_a, would_like, ensure, acceptances, parent=None)

    print ticket
