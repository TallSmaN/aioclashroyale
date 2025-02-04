from aiohttp import ClientTimeout

from aioclashroyale.client import AiohttpClient, Token
from aioclashroyale.const import *
from aioclashroyale.models.dto import (
    PaginatedList,
    Clan,
    ClanWarLog,
    RiverRaceLog,
    ClanMember,
    CurrentRiverRace,
    Player,
    UpcomingChests,
    Battle,
    FingerPrint,
    Items,
    TournamentHeader,
    Tournament,
    ClanRanking,
    PlayerRanking,
    PlayerPathOfLegendRanking,
    LeagueSeason,
    Location,
    LeagueSeasonV2,
    LadderTournamentRanking,
    ChallengeChain,
    Leaderboard,
    LadderTournament,
)


class AioClashRoyale:
    __slots__ = ('__client',)

    def __init__(self, token: Token, timeout: ClientTimeout = None, pretty_errors: bool = True) -> None:
        self.__client: AiohttpClient = AiohttpClient(token, timeout=timeout, pretty_errors=pretty_errors)

    async def get_clan_warlog(
            self,
            clan_tag: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> ClanWarLog:
        url: str = await CLAN_WAR_LOG.build_url(
            clan_tag,
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=ClanWarLog)

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
    ) -> PaginatedList[Clan]:
        url: str = await CLANS.build_url(
            name=name,
            location_id=location_id,
            min_members=min_members,
            max_members=max_members,
            min_score=min_score,
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=PaginatedList[Clan])

    async def get_clan_river_race_log(
            self,
            clan_tag: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> PaginatedList[RiverRaceLog]:
        url: str = await CLAN_RIVER_RACE_LOG.build_url(
            clan_tag,
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=PaginatedList[RiverRaceLog])

    async def get_clan(
            self,
            clan_tag: str
    ) -> Clan:
        url: str = await CLAN.build_url(
            clan_tag
        )

        return await self.__client.new_request(url, dto=Clan)

    async def get_clan_members(
            self,
            clan_tag: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> PaginatedList[ClanMember]:
        url: str = await CLAN_MEMBERS.build_url(
            clan_tag,
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=PaginatedList[ClanMember])

    async def get_current_river_race(
            self,
            clan_tag: str
    ) -> CurrentRiverRace:
        url: str = await CLAN_CURRENT_RIVER_RACE.build_url(
            clan_tag
        )

        return await self.__client.new_request(url, dto=CurrentRiverRace)

    async def get_player(
            self,
            player_tag: str
    ) -> Player:
        url: str = await PLAYER.build_url(
            player_tag
        )

        return await self.__client.new_request(url, dto=Player)

    async def get_player_upcoming_chests(
            self,
            player_tag: str
    ) -> UpcomingChests:
        url: str = await PLAYER_UPCOMING_CHESTS.build_url(
            player_tag
        )

        return await self.__client.new_request(url, dto=UpcomingChests)

    async def get_player_battle_log(
            self,
            player_tag: str
    ) -> list[Battle]:
        url: str = await PLAYER_BATTLE_LOG.build_url(
            player_tag
        )

        return await self.__client.new_request(url, dto=list[Battle])

    async def get_fingerprint(
            self,
            player_tag: str
    ) -> FingerPrint:
        url: str = await FINGERPRINT.build_url(
            player_tag
        )

        return await self.__client.new_request(url, dto=FingerPrint)

    async def get_cards(
            self,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> Items:
        url: str = await CARDS.build_url(
            limit=limit,
            after=after,
            before=before
        )
        return await self.__client.new_request(url, dto=Items)

    async def get_tournaments(
            self,
            name: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> PaginatedList[TournamentHeader]:
        url: str = await TOURNAMENTS.build_url(
            name=name,
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=PaginatedList[TournamentHeader])

    async def get_tournament(
            self,
            tournament_tag: str
    ) -> Tournament:
        url: str = await TOURNAMENT.build_url(
            tournament_tag,
        )

        return await self.__client.new_request(url, dto=Tournament)

    async def get_clan_rankings(
            self,
            location_id: int,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> PaginatedList[ClanRanking]:
        url: str = await LOCATION_CLAN_RANKINGS.build_url(
            location_id,
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=PaginatedList[ClanRanking])

    async def get_player_rankings(
            self,
            location_id: int,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> PaginatedList[PlayerRanking]:
        url: str = await LOCATION_PLAYER_RANKINGS.build_url(
            location_id,
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=PaginatedList[PlayerRanking])

    async def get_clan_war_rankings(
            self,
            location_id: int,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> PaginatedList[ClanRanking]:
        url: str = await LOCATION_CLAN_WAR_RANKINGS.build_url(
            location_id,
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=PaginatedList[ClanRanking])

    async def get_top_path_of_legend_players(
            self,
            season_id: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> PaginatedList[PlayerPathOfLegendRanking]:
        url: str = await LOCATION_PATH_OF_LEGEND_PLAYERS.build_url(
            season_id,
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=PaginatedList[PlayerPathOfLegendRanking])

    async def get_season(
            self,
            season_id: str
    ) -> LeagueSeason:
        url: str = await LOCATION_SEASON_INFO.build_url(
            season_id
        )

        return await self.__client.new_request(url, dto=LeagueSeason)

    async def get_top_player_rankings_for_season(
            self,
            season_id: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> PaginatedList[PlayerRanking]:
        url: str = await LOCATION_SEASON_RANKINGS.build_url(
            season_id,
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=PaginatedList[PlayerRanking])

    async def get_league_seasons(
            self
    ) -> PaginatedList[LeagueSeason]:
        url: str = await LOCATION_SEASONS.build_url()

        return await self.__client.new_request(url, dto=PaginatedList[LeagueSeason])

    async def get_locations(
            self,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> PaginatedList[Location]:
        url: str = await LOCATIONS.build_url(
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=PaginatedList[Location])

    async def get_league_seasons_v2(
            self
    ) -> PaginatedList[LeagueSeasonV2]:
        url: str = await LOCATION_SEASONS_V2.build_url()

        return await self.__client.new_request(url, dto=PaginatedList[LeagueSeasonV2])

    async def get_location_info(
            self,
            location_id: int
    ) -> Location:
        url: str = await LOCATION.build_url(
            location_id
        )

        return await self.__client.new_request(url, dto=Location)

    async def get_global_tournament_rankings(
            self,
            tournament_tag: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> PaginatedList[LadderTournamentRanking]:
        url: str = await LOCATION_TOURNAMENT_RANKINGS.build_url(
            tournament_tag,
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=PaginatedList[LadderTournamentRanking])

    async def get_player_rankings_in_path_of_legend(
            self,
            location_id: int,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> PaginatedList[PlayerPathOfLegendRanking]:
        url: str = await LOCATION_PATH_OF_LEGEND_PLAYERS_LOCAL.build_url(
            location_id,
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=PaginatedList[PlayerPathOfLegendRanking])

    async def get_challenges(
            self
    ) -> list[ChallengeChain]:
        url: str = await CHALLENGES.build_url()

        return await self.__client.new_request(url, dto=list[ChallengeChain])

    async def get_players_on_leaderboard(
            self,
            leaderboard_id: str,
            limit: int = None,
            after: str = None,
            before: str = None
    ) -> PaginatedList[Leaderboard]:
        url: str = await LEADERBOARD.build_url(
            leaderboard_id,
            limit=limit,
            after=after,
            before=before
        )

        return await self.__client.new_request(url, dto=PaginatedList[Leaderboard])

    async def get_leaderboards(
            self
    ) -> PaginatedList[Leaderboard]:
        url: str = await LEADERBOARDS.build_url()

        return await self.__client.new_request(url, dto=PaginatedList[Leaderboard])

    async def get_global_tournaments(
            self
    ) -> PaginatedList[LadderTournament]:
        url: str = await GLOBAL_TOURNAMENTS.build_url()

        return await self.__client.new_request(url, dto=PaginatedList[LadderTournament])
