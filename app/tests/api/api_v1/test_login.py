from fastapi.testclient import TestClient
from peewee import Database
from typing import Dict

from app.core.config import settings
from app.logger import logger


def test_get_access_token(client: TestClient) -> None:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]


def test_use_access_token(
        client: TestClient, superuser_token_headers: Dict[str, str]
) -> None:
    r = client.post(
        f"{settings.API_V1_STR}/login/test-token", headers=superuser_token_headers,
    )
    result = r.json()
    assert r.status_code == 200
    assert "email" in result


def test_use_access_token_denied(
        client: TestClient,
) -> None:
    a_token = ('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiw'
               'iZXhwIjoxNjU0ODkxODc1LCJqdGkiOiI0MGZhNDkyZDgxZmE0NGVhYjM5ZTU0ZjNlNmJkZjZh'
               'ZiIsInVzZXJfaWQiOjY2Nn0.5joqIGRWxrc-miwgidA54HZw6S1yAYfGB-u_qye1R38'
               )
    headers_ = {"Authorization": f"Bearer {a_token}"}
    r = client.post(
        f"{settings.API_V1_STR}/login/test-token", headers=headers_,
    )
    result = r.json()
    assert r.status_code == 401
    assert "not validate credentials" in result['detail']
