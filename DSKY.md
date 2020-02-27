# DSKY

A NOUN VERB language for expressing what you would like to do in your projects.
Read up about the history of [dsky](https://en.wikipedia.org/wiki/Apollo_Guidance_Computer#DSKY_interface)
on this anniversary year of Apollo 11!

## The Concept of DSKY 

The basic concept of Apollo 11's computer, DSKY, was that you can specify something you
want to do by specifying only a NOUN and a VERB.  This was all done with integers, which 
means they landed on the moon by giving their computer nothing but integers.  
But Kevin Bacon sure did look good when he was doing it.

### NOUNs

Presently git repos. `export GIT_HOST` into your ENV, or set it [perminantly]().

For any command, DSKY will:

* attempt to `cd` into ~/projects/$NOUN
* if the folder doesn't exist, it will try to go to your `$REPO` and download a project `$NOUN`.
* if it found the folder, it will attempt to `git fetch` to notify you of updates to the codebase.

#### $REPO

### VERBs

What would you like to do?

* isgo - PROJECT INITIALIZING - in a microservice world, why are you checking things out?
* Execute anything in it's `Makefile`. This is a great place to put
  * compile, test, package, deploy projects
* github - go to the project's github page
* (e)dit   - cd to the project's directory, and open your favorite $EDITOR

#### isgo

PROJECT INITIALIZING. This is core benefit to this system, and it involves several stages of 
your dev cycle. Let's say you decide to work on a project it could be yet another time, or
your very first time working on it.  Why do you have to distinguish? Just define the project,
which can usually be one name. This name is probably the project's name in git. This project
is `humane-api` or probably `trevorgrayson/humane-api` to you, since you're not working on it.

`dsky trevorgrayson/humane-api isgo will:

1. confirm the project is local on your computer. check it out if necessary. 
2. change to the directory of the project, as we will be working in it.
3. fetch any updates to the code base, and print them on screen when possible.
this is your "news" update for the project. what have your co-contributors been doing?
4. display the status of the current checkout. what did your forget to check in last time?
what weird branch are you on?
5. command prompt. get to work.

see the `install` section if you want to personalize this a bit better.


#### github

```
dsky $PROJECT_NAME github
```

general status of project

```
dsky $PROJECT_NAME stat
```

List of open PRs.

```
dsky $PROJECT_NAME pr
```

checkout remote branch or tag

```
dsky $PROJECT_NAME checkout $TAG
```

## install

IOU. this is a big one

### env variables

Here are some good variables to have set for these projects, or in general.

```
export PROJECTS=$HOME/projects
export GIT_HOST=git@github.com
export GIT_USER=grevrtrayson

alias dsky=". dsky" # will let dsky change your directory for you.
```

