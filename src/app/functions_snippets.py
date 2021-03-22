from bs4 import BeautifulSoup
import pandas as pd


class FunctionsSnippets(object):
    def __init__(self, html: str):
        self.html = html
        self.links = self.get_functions_links()


    def get_functions_links(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        links = [f"https://www.mql5.com{link.get('href')}" for link in soup.table.find_all('a')[::2]]
        return links

