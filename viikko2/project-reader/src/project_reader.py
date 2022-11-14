from urllib import request
from project import Project
import tomlkit


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        name = tomlkit.parse(content)['tool']['poetry']['name']
        desc = tomlkit.parse(content)['tool']['poetry']['description']
        dep = tomlkit.parse(content)['tool']['poetry']['dependencies']
        dev_dep = tomlkit.parse(content)['tool']['poetry']['dev-dependencies']
        dependencies = []
        dev_dependencies = []
        for key, value in dep.items():
            dependencies.append(key)
        for key, value in dev_dep.items():
            dev_dependencies.append(key)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, dependencies, dev_dependencies)
