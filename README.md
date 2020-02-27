# The Humane Developer API

A toolkit of shortcuts and integration points for developers.

## [DSKY](DSKY.md)

## runme

`runme` is a README.md file executor. `runme` will run through your readme file looking for
headers ("##") and map the code ( ``` delimited ) lines to their headings.

All commands will be prompted before execution. Hitting enter will run the command.

```
  # list sections
  runme

  # execute section
  runme section
```


## tkts

The intent of this is to give one set of commands that connect to any ticketing system.  
Presently the implementations are JIRA, or using the local file system. [More](./tkts/README.md)


## terminalize

Many commands come with a suite of methods which you may use consequtively, and may benefit from having a terminal 
experience.  Examples of this include `git`, `docker`, and several frameworks including `django`.

By running `terminalize` with the binary command as an argument, you can implement this.

```
  terminalize git
  git> fetch # runs `git fetch`
  git> diff # runs `git diff`

``` 

Some executables are looking for piped input. They can be implemented using `terminalize-pipe`

```
  terminalize-pipe "psql -h localhost"
  psql> select * from your_table;

```

This will be updated with useful features including command history and tab completion.

### Installation

The `bin` folder in this project needs to be in your `$PATH`.

```
  # export PROJECTS="~/projects"
	echo "export PATH=$PWD/bin/:$PATH" >> ~/.bash_profile
```

```
    # runme
    echo 'complete -W "`runme | paste -sd " " -`" runme' >> ~/.bash_profile

    # prj
    export HAPI_REPO="git@github.com:$YourName"
    echo 'alias prj=". prj"' >> ~/.bash_profile
    complete -W "`ls $PROJECTS`" hi


```

## Blue Sky
- ticketing: jira, trello, bugzilla, flat file
  - state changing -> code review
- software lifecycle
- version control
  - RSS: peer submissions
  - review
- news
- project planning
  - graphs
  - wiki pages
- chat?
- build status
