#from src.colour import Colour
from src.user import User
from src.repository import Repository

def getUserName() -> str:
    username = input("[USERNAME] - Enter your username: ")
    return username

def usernameExists(username: str) -> bool:
    return username is not None

def showOptions() -> None:
    print("[1] - SEE REPOSITORIES")
    print("[2] - SEE DATA")

def getUserOption() -> str:
    userOption = input("> ")
    return userOption

def showHeader() -> None:
    print()
    print()
    print("GITBEES II")
    print("By Marcello B.")
    print()
    print()

# 
# MAIN
#
def runGitbees() -> None:
    showHeader()
    username = getUserName()
    
    if usernameExists(username):
        userRepositories = Repository(username)
        userData = User(username)

    showOptions()
    userOption = getUserOption()
    
    if userOption == "1": userRepositories.doList()
    else: userData.showData()

runGitbees()