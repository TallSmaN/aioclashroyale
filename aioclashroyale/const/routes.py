from typing import Final

from aioclashroyale.client import Route

CLANS: Final[Route] = Route('/clans')
CLAN_INFO: Final[Route] = Route('/clans/{clan_tag}')
CLAN_MEMBERS: Final[Route] = Route('/clans/{clan_tag}/members')
CLAN_WAR_LOG: Final[Route] = Route('/clans/{clan_tag}/warlog')
CLAN_RIVER_RACE_LOG: Final[Route] = Route('/clans/{clan_tag}/riverracelog')
CLAN_CURRENT_WAR: Final[Route] = Route('/clans/{clan_tag}/currentwar')
CLAN_CURRENT_RIVER_RACE: Final[Route] = Route('/clans/{clan_tag}/currentriverrace')

PLAYER_INFO: Final[Route] = Route('/players/{player_tag}')
PLAYER_UPCOMING_CHESTS: Final[Route] = Route('/players/{player_tag}/upcomingchests')
PLAYER_BATTLE_LOG: Final[Route] = Route('/players/{player_tag}/battlelog')

FILES_FINGERPRINT: Final[Route] = Route('/files/fingerprint')

CARDS: Final[Route] = Route('/cards')

TOURNAMENTS: Final[Route] = Route('/tournaments')
TOURNAMENT_INFO: Final[Route] = Route('/tournaments/{tournament_tag}')

LOCATIONS: Final[Route] = Route('/locations')
LOCATION_INFO: Final[Route] = Route('/locations/{location_id}')
LOCATION_CLAN_RANKINGS: Final[Route] = Route('/locations/{location_id}/rankings/clans')
LOCATION_PLAYER_RANKINGS: Final[Route] = Route('/locations/{location_id}/rankings/players')
LOCATION_CLAN_WAR_RANKINGS: Final[Route] = Route('/locations/{location_id}/rankings/clanwars')
LOCATION_PATH_OF_LEGEND_PLAYERS: Final[Route] = Route('/locations/global/pathoflegend/{season_id}/rankings/players')
LOCATION_SEASON_INFO: Final[Route] = Route('/locations/global/seasons/{season_id}')
LOCATION_SEASON_RANKINGS: Final[Route] = Route('/locations/global/seasons/{season_id}/rankings/players')
LOCATION_SEASONS: Final[Route] = Route('/locations/global/seasons')
LOCATION_TOURNAMENT_RANKINGS: Final[Route] = Route('/locations/global/rankings/tournaments/{tournament_tag}')
LOCATION_PATH_OF_LEGEND_PLAYERS_LOCAL: Final[Route] = Route('/locations/{location_id}/pathoflegend/players')

CHALLENGES: Final[Route] = Route('/challenges')

LEADERBOARD: Final[Route] = Route('/leaderboard/{leaderboard_id}')
LEADERBOARDS: Final[Route] = Route('/leaderboards')

GLOBAL_TOURNAMENTS: Final[Route] = Route('/globaltournaments')
