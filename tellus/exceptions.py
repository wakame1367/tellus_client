# Reference:
# https://www.tellusxdp.com/ja/api-reference/


class APIException(Exception):
    """General unexpected response."""

    pass


class BadRequest(APIException):
    """Invalid request parameter, HTTP 400."""

    pass


class Unauthorized(APIException):
    """Authentication failed,  HTTP 401."""

    pass


class Forbidden(APIException):
    """You do not have access to the resource, HTTP 403."""

    pass


class NotFound(APIException):
    """The resource does not exist, HTTP 404."""

    pass


class MethodNotAllowed(APIException):
    """Requested methods are not supported, HTTP 405."""

    pass


class RequestTimeout(APIException):
    """The request timed out, HTTP 408."""

    pass


class LengthRequired(APIException):
    """Length is not included in the request header, HTTP 411."""

    pass


class RequestEntityTooLarge(APIException):
    """Request entity too large, HTTP 413."""

    pass


class InternalServerError(APIException):
    """An internal error has occurred, HTTP 500."""

    pass


class ServiceUnavailable(APIException):
    """Unable to use the service for some reason, HTTP 503."""

    pass
