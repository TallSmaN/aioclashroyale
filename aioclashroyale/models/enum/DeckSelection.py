from enum import Enum


class DeckSelection(Enum):
    COLLECTION: str = 'collection'
    DRAFT: str = 'draft'
    DRAFT_COMPETITIVE: str = 'draftCompetitive'
    PREDEFINED: str = 'predefined'
    EVENT_DECK: str = 'eventDeck'
    PICK: str = 'pick'
    WARDECK_PICK: str = 'wardeckPick'
    QUADDECK_PICK: str = 'quaddeckPick'
    UNKNOWN: str = 'unknown'