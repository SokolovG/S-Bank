import uvicorn

from litestar import Litestar
from database.connection import Base, engine, get_session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = Litestar(
    on_startup=[create_tables],
    dependencies={'sessions': get_session},
    debug=True
)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)