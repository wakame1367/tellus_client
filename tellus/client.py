from urllib.parse import urljoin

from requests import Request, Session

from .__version__ import __version__
from .auth import BearerAuth
from .constants import BASE_TILE_URL, RequestType, SatelliteID


def _get_user_agent():
    return f"tellus-client-python:{__version__}"


class BaseClient:
    satellite_id = SatelliteID.ASNARO_1
    api_version = "/api/v1"

    def __init__(self) -> None:
        _api = urljoin(self.api_version, self.satellite_id)
        self.base_url = urljoin(BASE_TILE_URL, _api)

    def search_scene(self, min_lat, min_lon, max_lat, max_lon):
        params = {
            "min_lat": min_lat,
            "min_lon": min_lon,
            "max_lat": max_lat,
            "max_lon": max_lon,
        }
        url = urljoin(self.base_url, "scene")
        resp = _do_request(RequestType.GET, url, params=params, headers={})
        return resp

    def get_scene(self, product_id: str):
        url = urljoin(self.base_url, f"get_scene/{product_id}")
        resp = _do_request(RequestType.GET, url, params={}, headers={})
        return resp


class SARCSatlient(BaseClient):
    def __init__(self) -> None:
        super().__init__()


class OptSatClient(BaseClient):
    def __init__(self) -> None:
        super().__init__()


class ASNARO1(SARCSatlient):
    satellite_id = SatelliteID.ASNARO_1

    def __init__(self) -> None:
        super().__init__()


class ASNARO2(SARCSatlient):
    satellite_id = SatelliteID.ASNARO_2

    def __init__(self) -> None:
        super().__init__()


class AVNIR2(OptSatClient):
    satellite_id = SatelliteID.AVINIR_2

    def __init__(self) -> None:
        super().__init__()


class TSUBAME(OptSatClient):
    satellite_id = SatelliteID.TSUBAME

    def __init__(self) -> None:
        super().__init__()


class PALSAR2(OptSatClient):
    satellite_id = SatelliteID.PALSAR_2

    def __init__(self) -> None:
        super().__init__()


def _do_request(method, url, params, data, headers):
    req = Request(
        method, url, params=params, data=data, headers=headers, auth=BearerAuth("")
    )
    with Session() as s:
        s.headers.update({"User-Agent": _get_user_agent()})
        resp = s.send(req.prepare())
    return resp
