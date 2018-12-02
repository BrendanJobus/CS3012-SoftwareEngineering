from github import Github, BadCredentialsException
import getpass
import sys

usr = input("Username: ")
pwd = getpass.getpass()

g = Github(usr, pwd)
try:
	print(g.get_user().id)
except BadCredentialsException:
	print("Invalid username or password.")
	sys.exit()

print("")
print("You have the following repos:")

repos = Github().get_user(usr).get_repos()
for repo in repos:
	print(repo.name)

while True:
	print("")
	repo_name = input("Pick a repo: ")

	if repo_name == "quit":
		break

	match = False
	selected_repo = None
	for repo in repos:
		if repo.name == repo_name:
			selected_repo = repo
			match = True
			break

	if match == False:
		print("That is not the name of any repo.")

	else:
		contributors = selected_repo.get_contributors()
		for c in contributors:
			print(c.name)

	print("")
	user_name = input("Pick a user: ")

	if user_name == "quit":
		break

	match = False
	selected_user = None
	for user in contributors:
		if user.name == user_name:
			selected_user = user
			match = True
			break

	if match == False:
		print("That is not the name of any user.")

	else:
		repos = selected_user.get_repos()
		for repo in repos:
			print(repo.name)
