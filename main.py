from config import TOKEN
from database.models import models_main
import asyncio

async def main():
    await models_main()

if __name__ == '__main__':
    asyncio.run(main())
