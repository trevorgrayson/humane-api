from github import issues


iss = issues()

an_issue = None
for issue in iss:
    print(issue['repository']['statuses_url'])
    an_issue = issue

print(an_issue)
