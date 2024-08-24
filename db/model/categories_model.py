import db.statements.categories_stmt as statements
from typing import List
from asyncpg import Record

async def get_categories(connection):
    result = await connection.fetch(statements.SELECT_CATEGORIES)
    return result