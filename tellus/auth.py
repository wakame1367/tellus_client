import os

import requests

ENV_API_KEY = "TELLUS_API_KEY"


class NotSetAPIKEY(Exception):
    pass


class Auth:
    def from_env(key_name: str) -> str:
        key_name = key_name or ENV_API_KEY
        api_key = os.getenv(key_name)
        if api_key is None:
            raise NotSetAPIKEY
        return api_key


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token: str):
        auth = Auth()
        token = auth.from_env(token)
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
