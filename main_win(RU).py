#Данные о сборке
print('Введите куда клонировать Git, пример: D:\Git')
clone_in=input()
print('Введите адрес репозитория Git, пример: https://github.com/SlyJackal/piska-bot.git')
clone_from=input()
print('Введите название репозитория, пример: piska-bot')
git_name=input()
print('Введите название ветки, пример: master')
fork_name=input()

#Скачать репозиторий
import git, os
if not os.path.isdir(clone_in + '/' + git_name):
   git.Git(clone_in).clone(clone_from)

#Получить сообщения из коммитов
repo = git.Repo('/'.join(str(x) for x in [clone_in,git_name]))
commits = repo.iter_commits(fork_name)
git_list_str=''
for commit in commits:
   git_list_str += commit.message

#Найти номера всех задач
import re
git_list = re.findall(r'\d{4,5}', git_list_str)

#Подключение модуля Jira
from jira import JIRA
from jira.client import JiraCookieAuth
#Получить доступ в Jira
print('Введите логин от Jira')
login=input()
#Через токен
print('Введите ваш токен')
token=input()
'''#Через пароль
print('Введите пароль от Jira')
password=input()'''

#Подключение к нашей Jira
jira_host='https://team-1602178802459.atlassian.net' '''Установить свой адрес'''
auth_jira = JIRA(jira_host, basic_auth=(login, token))

#Запрос списка задач у пользователя
print('Введите JQL запрос для выбора задач. Пример: project = AHEBURG order by created DESC')
jql_string=input()
jira_list = auth_jira.search_issues(jql_string)
issues_list=[]
for issue in jira_list:
  issues_list.append(issue.key.split('-')[1])

#Проверка списка задач в Git
res = [x for x in git_list + issues_list if x not in git_list]
print('В Git нет следующих доработок:', res)