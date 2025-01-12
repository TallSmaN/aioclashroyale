from enum import Enum


class PrivacyType(Enum):
    OPEN = "open"
    PASSWORD_PROTECTED = "password_protected"
    UNKNOWN = "unknown"