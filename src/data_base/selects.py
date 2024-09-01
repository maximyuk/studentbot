from src.data_base.create_db import BaseDBPart
from src.data_base.middleprocess import get_list

class SelectDB(BaseDBPart):    
    async def member_list(self):
        result = await self.cur.execute("SELECT `name_command` FROM `student_list`")
        return sorted(await get_list(result))
