from github import Github
import getpass

usr = input("Username: ")
pwd = getpass.getpass()

g = Github(usr, pwd)

print("")
print("{} has the following repos:".format(usr))

for repo in g.get_user().get_repos():
	print(repo.name)
