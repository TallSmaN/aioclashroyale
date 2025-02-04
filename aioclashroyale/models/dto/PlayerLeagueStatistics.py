from msgspec import Struct

from aioclashroyale.models.dto.LeagueSeasonResult import LeagueSeasonResult


class PlayerLeagueStatistics(Struct, rename='camel'):
    previous_season: LeagueSeasonResult = None
    current_season: LeagueSeasonResult = None
    best_season: LeagueSeasonResult = None