import aiohttp
from aiohttp_jinja2 import template
from sqlalchemy.sql import text

@template('index.html')
async def index(request):
    site_name = request.app['config'].get('site_name')
    return {'site_name': site_name}
try:
    async def post(request):
        async with request.app['db'].acquire() as conn:
            query = text("select * from users;")

            result = await conn.fetch(query)
            return aiohttp.web.Response(body=str(result))
except:
    print("Ошибка хендлер post")
