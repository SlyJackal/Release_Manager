#Download git
import git
git.Git("/home/slyjackal/Git").clone("https://github.com/SlyJackal/piska-bot.git")
#Get all messages from commits
import re
repo = git.Repo('/home/slyjackal/Git/piska-bot')
commits = repo.iter_commits('master')

git_list=''
for commit in commits:
    git_list += commit.message

result = re.findall(r'\d{4,5}', git_list)
print(result)

