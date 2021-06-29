#Download git
import git
git.Git("/home/slyjackal/Git").clone("https://github.com/SlyJackal/piska-bot.git")
#Get all messages from commits
import re
repo = git.Repo('/home/slyjackal/Git/piska-bot')
commits = repo.iter_commits('master')

git_list_str=''
for commit in commits:
    git_list_str += commit.message

git_list = re.findall(r'\d{4,5}', git_list_str)
#print(git_list)


jira_list = ['1234', '12345', '12345', '4444', '4444', '12345', '1234', '0000']
#Check lists
res = [x for x in git_list + jira_list if x not in jira_list]
print('В Git нет следующих доработок:', res)



