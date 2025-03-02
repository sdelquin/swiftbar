import datetime
import re


def parse_datetime(date: str, time: str, to_atlantic_canary: bool = True) -> datetime.datetime:
    TBC = '-- : --'
    clean_date = re.sub(r'^[^\d]+ *', '', date, flags=re.I)
    dt = datetime.datetime.strptime(clean_date, '%d.%m.%Y')
    if time != TBC:
        hours, minutes = map(int, time.split(':'))
        dt = dt.replace(hour=hours, minute=minutes)
        if to_atlantic_canary:
            dt -= datetime.timedelta(hours=1)
    return dt


def parse_teams(match: str, to_upper: bool = True) -> list[str]:
    teams = re.split(r' *VS *', match, flags=re.I)
    if to_upper:
        teams = [team.upper() for team in teams]
    return teams
