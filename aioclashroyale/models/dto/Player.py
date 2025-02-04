from msgspec import Struct

from aioclashroyale.models.dto.Arena import Arena
from aioclashroyale.models.dto.Item import Item
from aioclashroyale.models.dto.PathOfLegendSeasonResult import PathOfLegendSeasonResult
from aioclashroyale.models.dto.PlayerAchievementBadge import PlayerAchievementBadge
from aioclashroyale.models.dto.PlayerClan import PlayerClan
from aioclashroyale.models.dto.PlayerItemLevel import PlayerItemLevel
from aioclashroyale.models.dto.PlayerLeagueStatistics import PlayerLeagueStatistics
from aioclashroyale.models.enum.ClanRole import ClanRole


class Player(Struct, rename='camel'):
    clan: PlayerClan = None
    legacy_trophy_road_high_score: int = None
    current_deck: list[PlayerItemLevel] = None
    current_deck_support_cards: list[PlayerItemLevel] = None
    arena: Arena = None
    role: ClanRole = None
    wins: int = None
    losses: int = None
    total_donations: int = None
    league_statistics: PlayerLeagueStatistics = None
    cards: list[PlayerItemLevel] = None
    support_cards: list[PlayerItemLevel] = None
    current_favorite_card: Item = None
    badges: list[PlayerAchievementBadge] = None
    tag: str = None
    name: str = None
    exp_level: int = None
    trophies: int = None
    best_trophies: int = None
    donations: int = None
    donations_received: int = None
    achievements: list[PlayerAchievementBadge] = None
    battle_count: int = None
    three_crown_wins: int = None
    challange_cards_won: int = None
    challange_max_wins: int = None
    tournament_cards_won: int = None
    tournament_battle_count: int = None
    war_day_wins: int = None
    clan_cards_collected: int = None
    star_points: int = None
    exp_points: int = None
    total_exp_points: int = None
    last_path_of_legend_season_result: PathOfLegendSeasonResult = None
    best_path_of_legend_season_result: PathOfLegendSeasonResult = None
    progress: dict = None

