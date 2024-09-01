from aiosqlite import Cursor, Row
from typing import Iterable

async def get_list(lists: Cursor) -> list:
    lists: Iterable[Row] = await lists.fetchall()
    if not lists:
        return []

    return list(map(lambda e: e[0], lists))
