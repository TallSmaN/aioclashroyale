from aioclashroyale.const import CLAN_WAR_LOG, CLANS, LOCATIONS


class AioClashRoyale:
    def __init__(self, token: str) -> None:
        self.__token: str = token

    async def get_clans_clan_warlog(
            self,
            clan_tag: str,
            limit: int = None
            # after: str = None,
            # before: str = None,

    ) -> ...:
        return await CLAN_WAR_LOG.compile(clan_tag, limit=limit, min_members=5, location_id=234234, sadasd=None)

    async def get_clans(
            self,
            name: str = None,
            location_id: int = None,
            min_members: int = None,
            max_members: int = None,
            min_score: int = None,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ...: ...

    async def get_clan_river_race_log(
            self,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ...: ...

    async def get_clan_current_war(
            self,
            clan_tag: str
    ) -> ...: ...

    async def get_clan(
            self,
            clan_tag: str
    ) -> ...: ...

    async def get_clan_members(
            self,
            clan_tag: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ...: ...

    async def get_current_river_race(
            self,
            clan_tag: str
    ) -> ...: ...

    async def get_player_upcoming_chests(
            self,
            player_tag: str
    ) -> ...: ...

    async def get_player_battle_log(
            self,
            player_tag: str
    ) -> ...: ...

    async def get_player_fingerprint(
            self,
            player_tag: str
    ) -> ...: ...

    async def get_cards(
            self,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ...: ...

    async def get_tournaments(
            self,
            name: str = None,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ...: ...

    async def get_tournament(
            self,
            tournament_tag: str
    ) -> ...: ...

    async def get_clan_rankings_by_location(
            self,
            location_id: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ...: ...

    async def get_player_rankings_by_location(
            self,
            location_id: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ...: ...

    async def get_clan_war_rankings_by_location(
            self,
            location_id: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ...: ...

    async def get_top_path_of_legend_players(
            self,
            season_id: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ...: ...

    async def get_top_player_league_season(
            self,
            season_id: str
    ) -> ...: ...

    async def get_top_player_rankings_for_season(
            self,
            season_id: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ...: ...

    async def list_top_player_league_seasons(
            self
    ) -> ...: ...

    async def list_locations(
            self
    ) -> ...:
        return await LOCATIONS.compile()

    async def list_league_seasons_v2(
            self
    ) -> ...:
        ...

    async def get_location_info(
            self,
            location_id: str
    ) -> ...:
        ...

    async def get_global_tournament_rankings(
            self,
            tournament_tag: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ...:
        ...

    async def get_player_rankings_in_path_of_legend(
            self,
            location_id: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ...:
        ...

    async def get_current_and_upcoming_challenges(
            self
    ) -> ...:
        ...

    async def get_players_on_leaderboard(
            self,
            leaderboard_id: int,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ...:
        ...

    async def list_leaderboards(
            self
    ) -> ...:
        ...

    async def get_global_tournaments(
            self
    ) -> ...:
        ...
