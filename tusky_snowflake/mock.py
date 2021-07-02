"""
Mock snowflake generation for testing libraries realying on tusky_snowflake.

Usage:
    Assuming fake_service.py:
        >>> # fake_service.py
        >>> import tusky_snowflake
        >>> def name_service(name):
        >>>     id = tusky_snowflake.synchronous_get_snowflake()
        >>>     return {id: id,"name": name}

    Patch a single function:
        >>> # test_fake_service.py
        >>> import pytest; import tusky_snowflake; import fake_service
        >>> from unittest.mock import patch
        >>> @patch("fake_service.tusky_snowflake", tusky_snowflake.mock.new_snowflake_service())
        >>> def test_service(monkeypatch):
        >>>     actual = fake_service.name_service("Amy")
        >>>     expected = {"id": tusky_snowflake.Snowflake(1234), "name": "Amy"}
        >>>     assert actual == expected
"""
from ._snowflake import Snowflake


class _MockTuskySnowflake:
    def __init__(self):
        self._snowflake = Snowflake(1233)

    async def get_snowflake(self):
        self._snowflake = self._snowflake + 1
        return self._snowflake

    def synchronous_get_snowflake(self):
        self._snowflake = self._snowflake + 1
        return self._snowflake


def _snowflake_service_factory():
    while True:
        yield _MockTuskySnowflake()


_snowflake_services = _snowflake_service_factory()


def new_snowflake_service():
    return _snowflake_services.__next__()
