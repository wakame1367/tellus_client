import pytest

from tellus.auth import Auth, NotSetAPIKEY


def test_not_set_apikey():
    auth = Auth()
    with pytest.raises(NotSetAPIKEY):
        auth.from_env("")
