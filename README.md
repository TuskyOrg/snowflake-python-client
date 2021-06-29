# Snowflake
##### Python client for accessing Tusky's "snowflake" microservice
# WARNING ⚠: BREAKING CHANGES
This is a development build.
`get_snowflake`'s default uri will likely change for the production release. 
## Example
### Using Poetry
```
poetry add git+https://github.com/TuskyOrg/snowflake-python-client.git
```
## Example Usage
```python3
from typing import Any, Dict

import snowflake

async def create_item(title: str) -> Dict[str, Any]:
    id = await snowflake.get_snowflake()
    return {
        "id": id,
        "title": title
    }
```