# tkts

The intent of this is to give one set of commands that connect to any ticketing system.  
Presently JIRA is the only implementation.

## Commands

```
  # list tkts assigned to you
  tkts 

  # detail view
  tkts ID-<tab-complete><enter>

  # comment
  tkts ID-123 "I am the very comment of a modern major general."

  # create tkts
  tkts c[reate]<enter>

```

## Installation

`tkts` has a few requirements.

The `bin` folder in this project needs to be in your `$PATH`.

```
	echo "export PATH=$PWD/bin/:$PATH" >> ~/.bash_profile
```

An environment environment variable pointing to your jira server.  Consider adding this to your `~/.bash_profile`.

```
  export HAPI_TKTS="jira.$YourCompany.com:443"
```

While you're in your `~/.bash_profile` you can add tab completion with the following:

```
  echo "source $PWD/tkts/bash_profile" >> ~/.bash_profile
```

Finally, add a password file.

```
  echo "$username:$password" > ~/.jira_pass
  chmod 0600 ~/.jira_pass
```
