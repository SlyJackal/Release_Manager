#Get data
"""
print('Введите куда клонировать Git, пример: D:\Git')
clone_in=input()
print('Введите адрес репозитория Git, пример: https://github.com/SlyJackal/piska-bot.git')
clone_from=input()
print('Введите название репозитория, пример: piska-bot')
git_name=input()
print('Введите название ветки, пример: master')
fork_name=input()
"""
#Test data
clone_in='/home/slyjackal/Git'
#relative path '.\'
clone_from='https://github.com/SlyJackal/piska-bot.git'
git_name='piska-bot'
fork_name='master'


#Download git and get all messages from commits
import git, os

from jira.resources import Issue
if not os.path.isdir(clone_in + '/' + git_name):
   git.Git(clone_in).clone(clone_from)
repo = git.Repo('/'.join(str(x) for x in [clone_in,git_name]))
commits = repo.iter_commits(fork_name)
git_list_str=''
for commit in commits:
   git_list_str += commit.message

#Find numbers of tasks
import re
git_list = re.findall(r'\d{4,5}', git_list_str)

#Get tasks from jira
from jira import JIRA
from jira.client import JiraCookieAuth
#Acces to Jira
print('Введите логин от Jira')
login=input()

#By password
#print('Введите пароль от Jira')
#password=input()

#By token
print('Введите ваш токен')
token=input()
auth_jira = JIRA('https://team-1602178802459.atlassian.net', basic_auth=(login, token))
print('Введите JQL запрос для выбора задач')
jql_string='project = AHEBURG order by created DESC'
jira_list = auth_jira.search_issues(jql_string)
issues_list=[]
for issue in jira_list:
  issues_list.append(issue.key.split('-')[1])
print('Jira list:')
print(issues_list)
print('Git list:')
print(git_list)


#Check lists
res = [x for x in git_list + issues_list if x not in git_list]
print('В Git нет следующих доработок:', res)