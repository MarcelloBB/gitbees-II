import requests
import json
from colour import Colour

def showRepository(repositoryName): print(f"{Colour.cyan}[REPOSITORY] {Colour.blue}{repositoryName}")

class Repository:
    def __init__(self, user): self.user = user

    def __request(self):
        requestAddress = f"https://api.github.com/users/{self.user}/repos"
        response = requests.get(requestAddress)

        return response.json()
    
    def doList(self):
        response = self.__request()
        numberOfRepositories = range(len(response))

        for repository in numberOfRepositories:
            repositoryAddress = response[repository]['name']
            showRepository(repositoryAddress)
    

r = Repository("MarcelloBB")
r.doList()