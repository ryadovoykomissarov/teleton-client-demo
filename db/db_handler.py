from decouple import config

host = config('HOST')
port = config('PORT')
user = config('USER')
password = config('PASSWORD')
database = config('DB_NAME')

import asyncpg

async def get_connection():
    return await asyncpg.connect(host=host,
                                 port=port,
                                 user=user,
                                 database=database,
                                 password=password)

async def tear_down(connection):
    await connection.close()