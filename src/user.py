import requests
from colour import Colour
import json
    
def showUserData(login: str, name: str, location: str, bio: str,
                 followers: str, following: str, publicRepositories: str) -> None:
                
                print(f"{Colour.cyan}[LOGIN]                    -      {Colour.blue}{login}")
                print(f"{Colour.cyan}[NAME]                     -      {Colour.blue}{name}")
                print(f"{Colour.cyan}[LOCATION]                 -      {Colour.blue}{location}")
                print(f"{Colour.cyan}[BIO]                      -      {Colour.blue}{bio}")
                print(f"{Colour.cyan}[FOLLOWERS]                -      {Colour.blue}{followers}")
                print(f"{Colour.cyan}[FOLLOWING]                -      {Colour.blue}{following}")
                print(f"{Colour.cyan}[PUBLIC REPOSITORIES]      -      {Colour.blue}{publicRepositories}")

class User:
    def __init__(self, name: str) -> None: self.name = name

    def __request(self) -> str:
        requestAddress = f"https://api.github.com/users/{self.name}"
        response = requests.get(requestAddress)

        return response.json()

    def showData(self) -> None:
        response = self.__request()

        LOGIN = response['login']
        NAME = response['name']
        LOCATION = response['location']
        BIO = response['bio']
        FOLLOWERS = response['followers']
        FOLLOWING = response['following']
        PUBLIC_REPOSITORIES = response['public_repos']


        showUserData(LOGIN,
                    NAME,
                    LOCATION,
                    BIO,
                    FOLLOWERS,
                    FOLLOWING,
                    PUBLIC_REPOSITORIES)
                                            