import httplib
import json
import sys
import os
from base64 import b64encode

conn = httplib.HTTPSConnection(os.environ['HAPI_TKTS'])
b64 = b64encode( open(os.environ['HOME'] + '/.jira_pass').read()[:-1])

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Basic %s' % b64
}


def get_list():
    conn.request('GET', 
      '/rest/api/2/search?jql=assignee=trevor.grayson%20and%20resolution=Unresolved', {}, headers)
    resp = conn.getresponse()

    if resp.status != 200:
        print 'ERROR: %s' % resp.reason
        exit()
     
    body = resp.read()

    resp = json.loads(body)

    fp = open(os.environ['HOME'] +'/.jira_tickets', 'w')
    for issue in resp['issues']:
        fp.write(issue['key'] + '\n')
        print "\t".join([issue['key'],issue['fields']['summary']])

    print '%d issues' % resp['total'] 
    fp.close()


def get_issue(key):
    conn.request('GET', 
      '/rest/api/2/issue/%s' % key, {}, headers)
    resp = conn.getresponse()

    if resp.status != 200:
        print 'ERROR: %s' % resp.reason
        exit()
     
    body = resp.read()

    issue = json.loads(body)

    print "\t".join([issue['key'], issue['fields']['summary']])
    print
    print issue['fields']['description']


def create_issue(summary, as_a, would_like, ensure, acceptances, parent=None):
    create = {
        'fields': {
           'project': {
             'key': 'MP'
           },
           'summary': summary,
           'description': """
h1. User Story
As a {as_a} I want to {would_like} and ensure {ensure}.

h1. Acceptance Critera

- """.format(as_a=as_a, would_like=would_like, ensure=ensure) +\
"\n- ".join(acceptances)
           ,
           "issuetype": { "name": "Task" }
           # 'issuetype': { 'id': '5' }
        }
    }

    if parent is not None:
        create['fields']['parent'] = { 'key': parent }

    conn.request('POST', 
        '/rest/api/2/issue/',
        json.dumps(create), 
        headers)

    resp = conn.getresponse()
    print resp.status
    print resp.read()

def comment(issue_id, body):
   
   conn.request('POST', 
     '/rest/api/2/issue/{}/comment'.format(issue_id), 
     json.dumps({'body': body}), 
     headers)

   resp = conn.getresponse()

   if resp.status in ['201']:
       print 'ERROR: %s' % resp.reason
       exit()

