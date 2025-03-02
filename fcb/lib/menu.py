from swiftbarmenu import Menu as SwiftBarMenu

import settings
from lib.calendar import Calendar


class Menu:
    def __init__(self, calendar: Calendar, title: str = settings.MENU_TITLE):
        self.calendar = calendar
        self.menu = SwiftBarMenu(title)
        self.build()

    def build(self):
        first_match = self.calendar[0]
        title_suffix = (
            ':soccerball:' if first_match.match_today else f'({first_match.until_match_display})'
        )
        self.menu.header[0].text += f' {title_suffix}'
        self.menu.add_item(first_match.teams_display, color='orange')
        self.menu.add_item(first_match.datetime_display, color='orange')
        self.menu.add_item(first_match.competition)
        self.menu.add_item(first_match.tv_operator_display)
        self.menu.add_sep()
        for match in self.calendar[1:]:
            item = self.menu.add_item(match.teams_display)
            item.add_item(match.datetime_display)
            item.add_item(match.competition)
            item.add_item(match.tv_operator_display)

    def dump(self):
        self.menu.dump()
