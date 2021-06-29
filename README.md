# Snowflake
##### Python client for accessing Tusky's "snowflake" microservice
## Example
### Using Poetry
```
poetry add git+https://github.com/TuskyOrg/snowflake-python-client.git
```
## Example Usage
```python3
from typing import Any, Dict

import snowflake

get_snowflake = snowflake.setup_async("http://localhost:8080")

async def create_item(title: str) -> Dict[str, Any]:
    id = await get_snowflake()
    return {
        "id": id,
        "title": title
    }
```