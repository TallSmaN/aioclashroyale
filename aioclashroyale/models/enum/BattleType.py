from enum import Enum

class BattleType(Enum):
    PVP: str = "PvP"
    PVE: str = "PvE"
    CLANMATE: str = "clanMate"
    TOURNAMENT: str = "tournament"
    FRIENDLY: str = "friendly"
    SURVIVAL: str = "survival"
    PVP2V2: str = "pvp2V2"
    CLANMATE2V2: str = "clanMate2V2"
    CHALLENGE: str = "challenge"
    CHALLENGE2V2: str = "challenge2V2"
    CLANWAR_COLLECTION_DAY: str = "clanwarCollectionDay"
    CLANWAR_WAR_DAY: str = "clanwarWarDay"
    CASUAL_1V1: str = "casual1V1"
    CASUAL_2V2: str = "casual2V2"
    BOAT_BATTLE: str = "boatBattle"
    BOAT_BATTLE_PRACTICE: str = "boatBattlePractice"
    RIVER_RACE_PVP: str = "riverRacePvp"
    RIVER_RACE_DUEL: str = "riverRaceDuel"
    RIVER_RACE_DUEL_COLOSSEUM: str = "riverRaceDuelColosseum"
    TUTORIAL: str = "tutorial"
    PATH_OF_LEGEND: str = "pathOfLegend"
    SEASONAL_BATTLE: str = "seasonalBattle"
    PRACTICE: str = "practice"
    TRAIL: str = "trail"
    UNKNOWN: str = "unknown"
