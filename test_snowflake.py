import datetime
from unittest.mock import patch

import pytest

import _fake_service
import tusky_snowflake


@pytest.fixture()
def flake():
    return tusky_snowflake.Snowflake("43755317257211904")


def test_eq(flake: tusky_snowflake.Snowflake):
    assert flake == 43755317257211904
    another_flake = tusky_snowflake.Snowflake(43755317257211904)
    assert flake == another_flake


def test_time(flake: tusky_snowflake.Snowflake):
    assert flake.time == 2608020142
    assert flake.datetime == datetime.datetime(
        2021,
        6,
        29,
        20,
        30,
        1,
        420000,
    )


def test_msb(flake: tusky_snowflake.Snowflake):
    assert flake.msb == 0


def test_sequence(flake: tusky_snowflake.Snowflake):
    assert flake.sequence == 0


def test_machine_id(flake: tusky_snowflake.Snowflake):
    assert flake.machine_id == 1234


@patch("_fake_service.tusky_snowflake", tusky_snowflake.mock.new_snowflake_service())
def test_mock(monkeypatch):
        actual = _fake_service.name_service("Amy")
        expected = {"id": tusky_snowflake.Snowflake(1234), "name": "Amy"}
        assert actual == expected
        actual = _fake_service.name_service("Amy")
        expected = {"id": tusky_snowflake.Snowflake(1235), "name": "Amy"}
        assert actual == expected


@pytest.mark.asyncio
@patch("_fake_service.tusky_snowflake", tusky_snowflake.mock.new_snowflake_service())
async def test_patches_reset(monkeypatch):
    actual = _fake_service.name_service("Amy")
    expected = {"id": tusky_snowflake.Snowflake(1234), "name": "Amy"}
    assert actual == expected
    actual = await _fake_service.async_name_service("Amy")
    expected = {"id": tusky_snowflake.Snowflake(1235), "name": "Amy"}
    assert actual == expected


if __name__ == "__main__":
    pytest.main()
