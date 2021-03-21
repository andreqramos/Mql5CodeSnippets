from bs4 import BeautifulSoup
from src.app.parameter import Parameter

class Function(object):
    def __init__(self, html: str):
        soup = BeautifulSoup(html, 'html.parser')
        # name attribute
        self.name =  soup.find('span', class_='f_Functions').get_text()
        # type attribute
        self.type = soup.find('span', class_='f_Keywords').get_text()
        self.type = self.type.replace('\xa0','')
        self.type = self.type.replace(' ', '')
        self.parameters = self.get_parameters(html)


    def get_parameters(self, cell: str) -> list:
        soup = BeautifulSoup(cell, features="lxml")
        parameters_types = [x.get_text() for x in soup.find_all('span', class_='f_Keywords')][1:]
        parameters_names = [x.get_text() for x in soup.find_all('span', class_='f_Param')]
        parameters = [Parameter(x, y) for x, y in zip(parameters_names, parameters_types)]
        return parameters


    def get_snippet_body(self) -> str:
        snippet_body = f"{self.name}("
        for counter, parameter in enumerate(self.parameters, start=1):
            snippet_body += f"${{{counter}:{parameter}}}, "
        # remove the lasts',' and space
        snippet_body = snippet_body[:-2]
        snippet_body += ")$0"
        return [snippet_body]


    def to_snippet(self):
        snippet = {}
        snippet['prefix'] = f"{self.name}()"
        snippet['body'] = self.get_snippet_body()
        snippet['description'] = f"{self.name}() function"
        return snippet

