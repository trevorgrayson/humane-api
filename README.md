# hapi

The Human API.

- ticketing: jira, trello, bugzilla
  - state changing -> code review
  - project tkts
  - tickets created
- software lifecycle
- version control
  - RSS: peer submissions
  - review
- news
- project contexts
  - hi
- project planning
  - graphs
  - wiki pages
- chat?
- build status

## tkts

The intent of this is to give one set of commands that connect to any ticketing system.  
Presently JIRA is the only thing that is implemented.

`tkts` has two requirements.  

An environment environment variable pointing to your jira server.

```
    export HAPI_TKTS="jira.your-company.com:443"
```

Potentially a password file.   Presently JIRA only.

```
  echo "user-name:password" > ~/.jira_pass
  chmod 0600 ~/.jira_pass
```
