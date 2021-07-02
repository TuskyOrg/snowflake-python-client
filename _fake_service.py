""" Fake 3rd party service reliant on tusky_snowflake. Used for testing mocks. """
import tusky_snowflake


def name_service(name: str):
    id = tusky_snowflake.synchronous_get_snowflake()
    return {"id": id, "name": name}


async def async_name_service(name: str):
    id = await tusky_snowflake.get_snowflake()
    return {"id": id, "name": name}