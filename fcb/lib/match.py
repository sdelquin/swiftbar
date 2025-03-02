import datetime

from babel.dates import format_date

from .utils import parse_datetime, parse_teams


class Match:
    def __init__(
        self,
        date: str,
        time: str,
        match: str,
        competition: str,
        tv_operator: str,
    ):
        # Atlantic/Canary timezone
        self.datetime = parse_datetime(date, time)
        self.home_team, self.away_team = parse_teams(match)
        self.competition = competition.upper()
        self.tv_operator = tv_operator.upper() if tv_operator != '-' else None

    def __repr__(self):
        return f'{self.datetime} - {self.home_team} vs {self.away_team} ({self.competition})'

    @property
    def time_tbc(self) -> bool:
        return self.datetime.time() == datetime.time(0, 0)

    @property
    def until_match(self) -> datetime.timedelta:
        return self.datetime - datetime.datetime.now()

    @property
    def until_match_display(self) -> str:
        delta = self.until_match
        days = delta.days
        hours = delta.seconds // 3600
        if days < 1:
            return f'{hours}h'
        else:
            return f'{days}d'

    @property
    def date_display(self) -> str:
        return format_date(self.datetime, format='full', locale='es').capitalize()

    @property
    def time_display(self) -> str:
        if self.time_tbc:
            return 'Hora por confirmar'
        return self.datetime.strftime('%H:%Mh')

    @property
    def datetime_display(self) -> str:
        return f'{self.date_display} ({self.time_display})'

    @property
    def match_today(self) -> bool:
        return self.datetime.date() == datetime.date.today()

    @property
    def teams_display(self):
        return f'{self.home_team} vs {self.away_team}'

    @property
    def tv_operator_display(self):
        return self.tv_operator or 'Operador por confirmar'
