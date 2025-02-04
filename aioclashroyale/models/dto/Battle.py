from msgspec import Struct

from aioclashroyale.models.dto.Arena import Arena
from aioclashroyale.models.dto.GameMode import GameMode
from aioclashroyale.models.dto.PlayerBattleData import PlayerBattleData
from aioclashroyale.models.enum.BattleType import BattleType
from aioclashroyale.models.enum.DeckSelection import DeckSelection


class Battle(Struct, rename='camel'):
    game_mode: GameMode = None
    arena: Arena = None
    league_number: int = None
    team: list[PlayerBattleData] = None
    challenge_win_count_before: int = None
    boat_battle_side: str = None
    new_towers_destroyed: int = None
    prev_towers_destroyed: int = None
    remaining_towers: int = None
    deck_selection: DeckSelection = None
    opponents: list[PlayerBattleData] = None
    boat_battle_won: bool = None
    type: BattleType = None
    battle_time: str = None
    challange_id: int = None
    tournament_tag: str = None
    challenge_title: str = None
    is_ladder_tournament: bool = None
    is_hosted_match: bool = None



