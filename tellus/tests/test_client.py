import pytest

from tellus.auth import NotSetAPIKEY
from tellus.client import ASNARO1, ASNARO2, AVNIR2, PALSAR2, TSUBAME


@pytest.mark.parametrize("client", [ASNARO1, ASNARO2, AVNIR2, TSUBAME, PALSAR2])
def test_missing_api_key(client):
    cl = client()
    try:
        cl.get_scene("product_id")
    except NotSetAPIKEY:
        assert True
