from aiohttp import web
import aiohttp_jinja2
import jinja2
from .routes import setup_routes
import asyncpgsa




def create_app(config:dict):
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(app,
            loader = jinja2.PackageLoader('demo','temp')
    )
    setup_routes(app)
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)
    return app



#выполнить сразу после запуска приложение

async def on_start(app):
    config = app['config']
    pass
    #conectString = 'Driver={PostgreSQL ANSI};Server=localhost;Port=5432;Database=nexus;Uid=postgres;Pwd=postgres;'
    app['db'] = await  asyncpgsa.create_pool(dsn=config['database_url'])

#закрить после соединение
async def on_shutdown(app):
    await app['db'].close()
