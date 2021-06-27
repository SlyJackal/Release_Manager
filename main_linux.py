from re import split
#Download git
import git
git.Git("/home/slyjackal/Git").clone("https://github.com/SlyJackal/piska-bot.git")
#Get all messages from commits
repo = git.Repo('/home/slyjackal/Git/piska-bot')
commits = repo.iter_commits('master')
for commit in commits:
    a=(commit.message)
    print(a)
