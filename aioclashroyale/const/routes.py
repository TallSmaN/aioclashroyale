from typing import Final

from aioclashroyale.client import Route

__all__ = (
    'CLANS',
    'CLAN',
    'CLAN_MEMBERS',
    'CLAN_WAR_LOG',
    'CLAN_RIVER_RACE_LOG',
    'CLAN_CURRENT_RIVER_RACE',
    'PLAYER',
    'PLAYER_UPCOMING_CHESTS',
    'PLAYER_BATTLE_LOG',
    'FINGERPRINT',
    'CARDS',
    'TOURNAMENTS',
    'TOURNAMENT',
    'LOCATIONS',
    'LOCATION',
    'LOCATION_CLAN_RANKINGS',
    'LOCATION_PLAYER_RANKINGS',
    'LOCATION_CLAN_WAR_RANKINGS',
    'LOCATION_PATH_OF_LEGEND_PLAYERS',
    'LOCATION_SEASON_INFO',
    'LOCATION_SEASON_RANKINGS',
    'LOCATION_SEASONS',
    'LOCATION_SEASONS_V2',
    'LOCATION_TOURNAMENT_RANKINGS',
    'LOCATION_PATH_OF_LEGEND_PLAYERS_LOCAL',
    'CHALLENGES',
    'LEADERBOARD',
    'LEADERBOARDS',
    'GLOBAL_TOURNAMENTS'
)

CLANS: Final[Route] = Route('/clans')
CLAN: Final[Route] = Route('/clans/{0}')
CLAN_MEMBERS: Final[Route] = Route('/clans/{0}/members')
CLAN_WAR_LOG: Final[Route] = Route('/clans/{0}/warlog')
CLAN_RIVER_RACE_LOG: Final[Route] = Route('/clans/{0}/riverracelog')
CLAN_CURRENT_RIVER_RACE: Final[Route] = Route('/clans/{0}/currentriverrace')

PLAYER: Final[Route] = Route('/players/{0}')
PLAYER_UPCOMING_CHESTS: Final[Route] = Route('/players/{0}/upcomingchests')
PLAYER_BATTLE_LOG: Final[Route] = Route('/players/{0}/battlelog')

FINGERPRINT: Final[Route] = Route('/files/fingerprint')

CARDS: Final[Route] = Route('/cards')

TOURNAMENTS: Final[Route] = Route('/tournaments')
TOURNAMENT: Final[Route] = Route('/tournaments/{0}')

LOCATIONS: Final[Route] = Route('/locations')
LOCATION: Final[Route] = Route('/locations/{0}')
LOCATION_CLAN_RANKINGS: Final[Route] = Route('/locations/{0}/rankings/clans')
LOCATION_PLAYER_RANKINGS: Final[Route] = Route('/locations/{0}/rankings/players')
LOCATION_CLAN_WAR_RANKINGS: Final[Route] = Route('/locations/{0}/rankings/clanwars')
LOCATION_PATH_OF_LEGEND_PLAYERS: Final[Route] = Route('/locations/global/pathoflegend/{0}/rankings/players')
LOCATION_SEASON_INFO: Final[Route] = Route('/locations/global/seasons/{0}')
LOCATION_SEASON_RANKINGS: Final[Route] = Route('/locations/global/seasons/{0}/rankings/players')
LOCATION_SEASONS: Final[Route] = Route('/locations/global/seasons')
LOCATION_SEASONS_V2: Final[Route] = Route('/locations/global/seasonsV2')
LOCATION_TOURNAMENT_RANKINGS: Final[Route] = Route('/locations/global/rankings/tournaments/{0}')
LOCATION_PATH_OF_LEGEND_PLAYERS_LOCAL: Final[Route] = Route('/locations/{0}/pathoflegend/players')

CHALLENGES: Final[Route] = Route('/challenges')

LEADERBOARD: Final[Route] = Route('/leaderboard/{0}')
LEADERBOARDS: Final[Route] = Route('/leaderboards')

GLOBAL_TOURNAMENTS: Final[Route] = Route('/globaltournaments')
