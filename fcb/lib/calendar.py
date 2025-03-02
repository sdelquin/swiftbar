import requests
from bs4 import BeautifulSoup

import settings
from lib.match import Match


class Calendar:
    def __init__(self):
        self.matches = self.load_matches()

    def load_matches(self) -> list[Match]:
        self.matches = []
        response = requests.get(settings.MATCHES_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        if table := soup.select_one(settings.MATCHES_SELECTOR):
            for row in table.select('tbody tr:not(.row-more-info):not(.promotion)'):
                match_info = [td.get_text() for td in row.find_all('td')]
                match_info.pop()
                match = Match(*match_info)
                self.matches.append(match)
        return self.matches

    def __iter__(self):
        return iter(self.matches)

    def __getitem__(self, index):
        return self.matches[index]

    def __slice__(self, start, stop):
        return self.matches[start:stop]
