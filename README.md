# The Humane Developer API

A toolkit of shortcuts and integration points for developers.

## env variables

Here are some good variables to have set for these projects, or in general.

```
export PROJECTS=$HOME/projects
```

## prj

`prj` is how you start working on a *project*.

A project correlate with a git repo.  A presumption is presently being made that you are working out of the `~/projects` folder. *TODO*

The purpose of the `prj` command is to:

- get you into the correct directory to work on the project 
- install the project from git, if it isn't downloaded yet
- if installed, find new updates to the project
- start up any virtual environment needed to develop the project
- potentially run health/testing on the project to get status (future feature)

```
  prj project_name
```

This will 

* attempt to `cd` into ~/projects/project_name
* if the folder doesn't exist, it will try to go to your `HAPI_REPO` and download a project of `project_name`.
* if it found the folder, it will attempt to `git fetch` to notify you of other developer's updates to the codebase.
* if it finds a folder named `~/.venv/project_name`, it will attempt to start a python `virtualenv` with it.

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
