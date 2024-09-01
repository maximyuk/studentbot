from typing import Literal

from src.data_base.create_db import BaseDBPart


class AddDB(BaseDBPart):
    async def add_student_group(self, name_member, donate):
        await self.cur.execute(
            "INSERT INTO `student_list` (`name_member`, `donate`) VALUES (?,?)",
            (name_member, donate),
        )
        return await self.base.commit()