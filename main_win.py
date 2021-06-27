from re import split
#Download git
import git
git.Git("D:/GitHub").clone("https://github.com/SlyJackal/piska-bot.git")
#Get all messages from commits
repo = git.Repo('D:/GitHub/piska-bot')
commits = repo.iter_commits('master')
how_many=(len(commits))
print('Всего коммитов:', how_many)
for commit in commits:
    a=[commit.message]
    print(a)
