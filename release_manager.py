import git
import os
import re
import argparse
from jira import JIRA



#Создание аргументов
parser = argparse.ArgumentParser()
parser.add_argument("-jira_user", dest="user", required=True)
parser.add_argument("-jira_pass", dest="jira_jpass", required=True)
args = parser.parse_args()
print(args)




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
if not os.path.isdir(clone_in + '/' + git_name):
   git.Git(clone_in).clone(clone_from)

#Получить сообщения из коммитов
repo = git.Repo('/'.join(str(x) for x in [clone_in,git_name]))
commits = repo.iter_commits(fork_name)
git_list_str=''
for commit in commits:
   git_list_str += commit.message

#Найти номера всех задач
git_list = re.findall(r'\d{4,5}', git_list_str)


#Получить доступ в Jira
login=user

#Через пароль
password=jira_pass

#Подключение к нашей Jira
jira_host='https://team-1602178802459.atlassian.net' '''Установить свой адрес'''
auth_jira = JIRA(jira_host, auth=(login, password))

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