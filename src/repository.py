import requests
import json
from colour import Colour

def showRepository(repositoryName: str) -> None: print(f"{Colour.cyan}[REPOSITORY] {Colour.blue}{repositoryName}")

class Repository:
    def __init__(self, user: str) -> None: self.user = user

    def __request(self) -> str:
        requestAddress = f"https://api.github.com/users/{self.user}/repos"
        response = requests.get(requestAddress)

        return response.json()
    
    def doList(self) -> None:
        response = self.__request()
        numberOfRepositories = range(len(response))

        for repository in numberOfRepositories:
            repositoryAddress = response[repository]['name']
            showRepository(repositoryAddress)
    
    