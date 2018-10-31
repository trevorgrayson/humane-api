import jira

SERVICE = jira

def reported():
    SERVICE.reported()

def get_list():
    SERVICE.get_list()

def get_issue(key):
    SERVICE.get_issue(key)

def comment(issue_id, body):
    SERVICE.comment(issue_id, body)

def create_issue(summary, as_a, would_like, ensure, acceptances, parent=None):
    SERVICE.create_issue(summary, as_a, would_like, ensure, acceptances, parent=None)
