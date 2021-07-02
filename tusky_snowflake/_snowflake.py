import datetime

import httpx


class Snowflake(int):
    # The full word "bit_length" was chosen over "bit_len"
    # to remain similar to int's  built-in method "bit_length"
    _BIT_LENGTH_TIME = 39
    _BIT_LENGTH_SEQUENCE = 11
    _BIT_LENGTH_MACHINE_ID = 13

    _MASK_MACHINE_ID = (
        16775168  # (1 << (_BIT_LENGTH_MACHINE_ID - 1)) << _BIT_LENGTH_SEQUENCE
    )
    _MASK_SEQUENCE = 2047  # 1 << _BIT_LENGTH_SEQUENCE - 1

    _TUSKY_EPOCH = datetime.datetime(year=2020, month=9, day=1).timestamp()

    @property
    def time(self) -> int:
        return self >> (self._BIT_LENGTH_SEQUENCE + self._BIT_LENGTH_MACHINE_ID)

    @property
    def datetime(self) -> datetime.datetime:
        # This snowflake implementation increments every 10 milliseconds
        seconds_since_tusky_epoch = self.time / 100
        # This SHOULD return timezone = UTC+0, but timezones are complicated
        return datetime.datetime.fromtimestamp(
            seconds_since_tusky_epoch + self._TUSKY_EPOCH,
        )

    @property
    def msb(self) -> int:
        """Most significant bit"""
        return self >> 63

    @property
    def sequence(self) -> int:
        return self & self._MASK_SEQUENCE

    @property
    def machine_id(self) -> int:
        return (self & self._MASK_MACHINE_ID) >> self._BIT_LENGTH_SEQUENCE


async def get_snowflake(uri="http://host.docker.internal:8080") -> Snowflake:
    async with httpx.AsyncClient() as client:
        r = await client.get(uri)
    r.raise_for_status()
    return Snowflake(r.json()["id"])


def synchronous_get_snowflake(uri="http://host.docker.internal:8080") -> Snowflake:
    r = httpx.get(uri)
    r.raise_for_status()
    return Snowflake(r.json()["id"])
