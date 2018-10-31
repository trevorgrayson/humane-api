# hapi

The Human API. A toolkit of bash shortcuts for developers.

## tkts

The intent of this is to give one set of commands that connect to any ticketing system.  
Presently JIRA is the only implementation.

### Commands

```
  # list tkts assigned to you
  tkts 

  # detail view
  tkts ID-<tab-complete><enter>

  # comment
  tkts ID-123 "I am the very comment of a modern major general."

  # create tkts
  tkts c[reate]

# comment
```

### `tkts` Installation

`tkts` has a few requirements.

An environment environment variable pointing to your jira server.  Consider adding this to your `~/.bash_profile`.

```
    export HAPI_TKTS="jira.your-company.com:443"
```

While you're in your `~/.bash_profile` you can add tab completion with the following:

```
  echo "source $PWD/bash/bash_profile" >> ~/.bash_profile
```

Finally, add a password file.

```
  echo "$user-name:$password" > ~/.jira_pass
  chmod 0600 ~/.jira_pass
```


- ticketing: jira, trello, bugzilla, flat file
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
