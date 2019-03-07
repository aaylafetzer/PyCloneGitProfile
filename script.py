import os, sys, requests, json, threading

GIT = None

def Clone(git, repo): #Run git clone command
    os.system("git clone " + '/'.join(['https:/','github.com',git,repo,]) + ".git %USERPROFILE%\\Documents\\Code\\" + repo)

def ParseJson(json):
    return json.json()

if (len(sys.argv) == 1): #Test if a profile name is given in the system arguments
    GIT = input("Github username: ")
else: #Nothing was provided
    GIT = sys.argv[1]

repos = ParseJson(requests.get("http://api.github.com/users/" + GIT + "/repos"))
os.system("cd /d ")
for i in repos:
    threading.Thread(target=Clone, args=(GIT, i["name"])).start()