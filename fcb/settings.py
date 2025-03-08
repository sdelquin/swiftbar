from prettyconf import config

MATCHES_URL = config(
    'MATCHES_URL', default='https://www.laliga.com/clubes/fc-barcelona/proximos-partidos'
)

MATCHES_SELECTOR = config(
    'MATCHES_SELECTOR',
    default='#__next > div.styled__ClubContainer-sc-zdygb8-0.kEuFAc > div.styled__ClubSectionContent-sc-zdygb8-8.bDNocp > div > div.styled__ContainerMax-sc-1ba2tmq-0.esSirm > div > div:nth-child(1) > div > table',
)

MENU_TITLE = config('MENU_TITLE', default='FCB')

TODAY_MATCH_COLOR = config('TODAY_MATCH_COLOR', default='green')
NEXT_MATCH_COLOR = config('NEXT_MATCH_COLOR', default='orange')
