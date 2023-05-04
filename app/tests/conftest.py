import pytest
from fastapi.testclient import TestClient
from peewee import SqliteDatabase, Database
from playhouse.reflection import Introspector
from typing import Dict, Generator

from app.app import app
from app.core.config import settings
from app.db import db as db_from_app
# from app.tests.utils.user import authentication_token_from_email
from app.tests.utils.utils import get_superuser_token_headers


@pytest.fixture(scope="module")
def db() -> Generator:
    db_from_app.session_start()
    yield db_from_app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def superuser_token_headers(client: TestClient) -> Dict[str, str]:
    return get_superuser_token_headers(client)

# @pytest.fixture(scope="module")
# def normal_user_token_headers(client: TestClient, db: Database) -> Dict[str, str]:
#     return authentication_token_from_email(
#         client=client, email=settings.EMAIL_TEST_USER, db=db
#     )
