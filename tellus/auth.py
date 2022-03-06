import logging
import os
from typing import Optional

import requests

LOGGER = logging.getLogger(__name__)

ENV_API_KEY = "TELLUS_API_KEY"


class Auth:
    def from_env(key_name: Optional[str] = None) -> str:
        key_name = key_name or ENV_API_KEY
        api_key = os.getenv(key_name)
        return api_key


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token: Optional[str] = None):
        auth = Auth()
        token = auth.from_env(token)
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r