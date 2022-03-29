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
JIRA_URL_REST_API = r'http://jira.cbr.ru/rest/api/2'

# Замена некорректных символов, которые могут встречаться в полях issue в Jira
def replace_incorrect_charset_symbols(info):
    return info.encode('cp1251', errors='replace').decode('cp1251') if info else ' '


def parser_command_line_arguments():
    """объявление парсера для внешнего параметра"""
    parser = argparse.ArgumentParser(description='build version script')
    parser.add_argument('file_name', help='file name report')
    return parser


def get_requests(url):
    if not JIRA_AUTH:
        logger.error('System environment JIRA_AUTH not set!')
        sys.exit(1)
    return requests.get(url, headers={'Authorization': 'Basic %s' % JIRA_AUTH})


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