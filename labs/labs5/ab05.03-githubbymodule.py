from github import Github
from config import config as cfg
import requests
# 3. Test that your pyGithub works
apikey = cfg["githubkey"]
# use your own key
g = Github(apikey)
for repo in g.get_user().get_repos():
 print(repo.name)
# 4. Modify the program to get the clone URL of a repository on your account (you could make
# a private one just for this if you wish). Put a file in the repository called test.txt
g = Github(apikey)
repo = g.get_repo("clydewatts1/test")
print(repo.clone_url)
#5. Get the download URL of the file in this repository called test.txt (make sure that there is a
#file called test.txt in there
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)
# 6. I would comment out the print statements once you are happy the program is working
#7.Use the download URL to make a http request to the file can output the contents of the file
#(TEXT contents).
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)