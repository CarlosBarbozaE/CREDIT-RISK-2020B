import json
from typing import List

import requests
from bs4 import BeautifulSoup


class AbstractIndustry:

    def __init__(self, title: str, children: List['AbstractIndustry']):
        self.title = title
        self.children = children

    def __repr__(self):
        return f"<{self.level}, {self.title}>"

    @property
    def level(self):
        raise NotImplementedError

    def add_child(self, child: 'AbstractIndustry'):
        self.children.append(child)

    def to_dict(self):
        return {
            "title": self.title,
            "level": self.level,
            "children": [
                child.to_dict()
                for child in self.children
            ]
        }

    @staticmethod
    def from_dict(**kwargs):
        raise NotImplementedError

    def jsonify(self) -> str:
        return json.dumps(self.to_dict(), indent=4)


class Division(AbstractIndustry):
    level = "SIC Division"

    @staticmethod
    def from_dict(**kwargs):
        return Division(
            title=kwargs["title"],
            children=[
                MajorGroup.from_dict(**k)
                for k in kwargs.get("children", [])
            ]
        )


class MajorGroup(AbstractIndustry):
    level = "SIC Major Group"

    @staticmethod
    def from_dict(**kwargs):
        return MajorGroup(
            title=kwargs["title"],
            children=[
                Group.from_dict(**k)
                for k in kwargs.get("children", [])
            ]
        )

    @staticmethod
    def from_url(url):
        response = requests.get(url)
        html = BeautifulSoup(response.text, "html.parser")
        return MajorGroup(
            title=[
                elm.text
                for elm in html.find_all("h2")
                if elm.text.lower().startswith("major group")][0],
            children=[
                Group(
                    title=group.text,
                    children=[
                        Single(
                            title=single.parent.text,
                            children=[]
                        )
                        for single in html.find_all("a")
                        if single.attrs.get("href", "").startswith("sic_manual")
                        and single.parent.text.startswith(group.text.split(":")[0].split(" ")[-1])
                    ]
                )
                for group in html.find_all("strong")
                if group.text.lower().startswith("industry group")
            ]
        )


class Group(AbstractIndustry):
    level = "SIC Group"

    @staticmethod
    def from_dict(**kwargs):
        return Group(
            title=kwargs["title"],
            children=[
                Single.from_dict(**k)
                for k in kwargs.get("children", [])
            ]
        )


class Single(AbstractIndustry):
    level = "SIC Single Industry"

    @staticmethod
    def from_dict(**kwargs):
        return Single(title=kwargs["title"], children=[])


class SIC(AbstractIndustry):
    level = "Standard Industry Classification"

    @staticmethod
    def from_dict(**kwargs):
        return SIC(
            title=kwargs["title"],
            children=[
                Division.from_dict(**k)
                for k in kwargs.get("children", [])
            ]
        )

    @staticmethod
    def from_url(url: str) -> 'SIC':
        response = requests.get(url)
        html = BeautifulSoup(response.text, "html.parser")
        divisions = []
        for element in html.find_all("a"):
            href = element.attrs.get("href", "")
            title = element.attrs.get("title", "")
            if not href.startswith("sic_manual"):
                continue
            elif href.endswith("division"):
                div = Division(title=title, children=[])
                divisions.append(div)
            elif href.endswith("group"):
                major_group_url = url.replace("sic_manual.html", href)
                divisions[-1].add_child(MajorGroup.from_url(url=major_group_url))
        return SIC(title="SIC", children=divisions)
