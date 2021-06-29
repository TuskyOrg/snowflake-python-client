import datetime


import pytest

import snowflake


@pytest.fixture()
def flake():
    return snowflake.Snowflake("43755317257211904")


def test_eq(flake: snowflake.Snowflake):
    assert flake == 43755317257211904
    another_flake = snowflake.Snowflake(43755317257211904)
    assert flake == another_flake


def test_time(flake: snowflake.Snowflake):
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


def test_msb(flake: snowflake.Snowflake):
    assert flake.msb == 0


def test_sequence(flake: snowflake.Snowflake):
    assert flake.sequence == 0


def test_machine_id(flake: snowflake.Snowflake):
    assert flake.machine_id == 1234


if __name__ == "__main__":
    pytest.main()
