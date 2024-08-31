import os

import aiosqlite
import asyncache

from src.data_base.adds import AddDB




class Database(AddDB):
    @classmethod
    @asyncache.cached({})
    async def setup(cls):
        if not os.path.exists("data"):
            os.mkdir("data")

        base = await aiosqlite.connect("data/database.db")
        cur = await base.cursor()

        if base:
            print("DATA BASE CONNECTED")


        await base.execute(
            """
            CREATE TABLE IF NOT EXISTS student_list(
                id         INTEGER PRIMARY KEY,
                name_command TEXT NOT NULL,
                donate INTEGER DEFAULT 0
            )
            """
        )
        
        
        return cls(base, cur)