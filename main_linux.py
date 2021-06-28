import re
#re.split and re.sub
#Download git
import git
#git.Git("/home/slyjackal/Git").clone("https://github.com/SlyJackal/piska-bot.git")
#Get all messages from commits
repo = git.Repo('/home/slyjackal/Git/piska-bot')
commits = repo.iter_commits('master')

git_list=[]
for commit in commits:
    git_result=(', '.join(map(str, commit.message)))
    git_list.append(re.findall(r'\d{4,5}', (git_result)))
   
#git_result=(', '.join(map(str, git_list)))
print(git_list)
#Find all numbers
#find from 4 to 5 numbers \d{4,5}
#task_list = re.search(r'\d{4,5}', r=a)
#task_list = re.search(r'\b[горь]\, git_list)
#print (task_list.group(0))
# if re.search(r'\d{4,5}\d', git_list) is not None:
#        print('I find')