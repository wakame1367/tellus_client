from enum import Enum

BASE_TILE_URL = "https://gisapi.tellusxdp.com"


class RequestType(Enum):
    """Enum constant class for GET/POST request type."""

    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"
    PATCH = "PATCH"


class SatelliteID(Enum):
    """Satellite identifier used in tellus api."""

    AVINIR_2 = "av2ori"
    ASNARO_1 = "asnaro1"
    ASNARO_2 = "asnaro2"
    TSUBAME = "tsubame"
    LANDSAT_8 = "landsat8"
    PALSAR_2 = "palsar2"
