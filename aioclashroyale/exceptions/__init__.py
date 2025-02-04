__all__ = (
    'BadRequestException',
    'ForbiddenException',
    'NotFoundException',
    'TooManyRequestsException',
    'InternalServerException',
    'ServiceUnavailableException',
    'EXCEPTION_MAP'
)


class AioClashRoyaleException(Exception):
    def __init__(self, exception_data: dict) -> None:
        super().__init__(f'Reason: {exception_data['reason']}\nMessage: {exception_data['message']}')


class BadRequestException(AioClashRoyaleException):
    """
    Exception class for bad requests.

    This exception is raised when a request is invalid or cannot be processed.
    """


class ForbiddenException(AioClashRoyaleException):
    """
    Exception class for forbidden requests.

    This exception is raised when a request is forbidden or access is denied.
    """


class NotFoundException(AioClashRoyaleException):
    """
    Exception class for not found requests.

    This exception is raised when a requested resource is not found.
    """


class TooManyRequestsException(AioClashRoyaleException):
    """
    Exception class for too many requests.

    This exception is raised when too many requests are made within a certain time frame.
    """


class InternalServerException(AioClashRoyaleException):
    """
    Exception class for internal server errors.

    This exception is raised when an internal server error occurs.
    """


class ServiceUnavailableException(AioClashRoyaleException):
    """
    Exception class for service unavailable.

    This exception is raised when the service is unavailable.
    """


EXCEPTION_MAP: dict[int, type[Exception]] = {
    400: BadRequestException,
    403: ForbiddenException,
    404: NotFoundException,
    429: TooManyRequestsException,
    500: InternalServerException,
    503: ServiceUnavailableException,
}
