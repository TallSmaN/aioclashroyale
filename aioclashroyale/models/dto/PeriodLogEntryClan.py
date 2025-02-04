from msgspec import Struct


class PeriodLogEntryClan(Struct, rename='camel'):
    tag: str = None