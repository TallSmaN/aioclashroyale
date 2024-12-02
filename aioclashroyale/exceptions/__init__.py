
class AioClashRoyaleException(Exception):
    """
    Base exception class for AioClashRoyale.

    Attributes:
        reason (str): The reason for the exception.
        message (str): The message associated with the exception.
    """

    def __init__(self, reason: str, message: str) -> None:
        """
        Initializes the AioClashRoyaleException.

        Args:
            reason (str): The reason for the exception.
            message (str): The message associated with the exception.
        """
        super().__init__(f'Reason: {reason}\nMessage: {message}')



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



__all__ = (
    'BadRequestException',
    'ForbiddenException',
    'NotFoundException',
    'TooManyRequestsException',
    'InternalServerException',
    'ServiceUnavailableException',
)