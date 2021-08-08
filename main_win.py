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
clone_in='D:\Git'
#relative path '.\'
clone_from='https://github.com/SlyJackal/piska-bot.git'
git_name='piska-bot'
fork_name='master'


#Download git and get all messages from commits
import git
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
jac = JIRA('https://jira.atlassian.com')
#Acces to Jira
print('Введите логин от Jira')
login=input()
print('Введите пароль от Jira')
password=input()
auth_jira = JIRA(basic_auth=(login, password))

print('Введите JQL запрос для выбора задач')
JQL=input()
jira_list = [JiraCookieAuth.search_issues(JQL)]
jira_list = ['1234', '12345', '12345', '4444', '4444', '12345', '1234', '0000']

#Check lists
res = [x for x in git_list + jira_list if x not in jira_list]
print('В Git нет следующих доработок:', res)