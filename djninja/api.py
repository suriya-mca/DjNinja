# import router package
from ninja import Router
import asyncio
import asyncpg

# router instance
router = Router()

@router.get("/home")
async def home(request):
    return {'test': 'success'}

@router.get("/pg")
async def run(request):
    conn = await asyncpg.connect(user='postgres', password='Fate1234',
                                 database='postgres', host='127.0.0.1')
    values = await conn.execute('''
        CREATE TABLE sample(
            id serial PRIMARY KEY,
            name text,
            dob date
        )
    ''')
    await conn.close()
    print("done")


# run server -> uvicorn core.asgi:application --reload 
