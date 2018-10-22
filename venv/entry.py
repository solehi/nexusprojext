import argparse
import aiohttp
import asyncio
from demo import create_app
from demo.settings import load_config

#uvloop для того что бы проект работал быстее
try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print("Library uvloop is not available")

#переменные

parser = argparse.ArgumentParser(description="Nexus Project")
parser.add_argument('--host',help = "host to listen")
parser.add_argument('--post',help="Posrt to accept connection")
parser.add_argument("-c","--config", type=argparse.FileType('r'),
    help="Path to configuration file"
)

args = parser.parse_args()
app = create_app(config = load_config(args.config))

if __name__ == '__main__':
    aiohttp.web.run_app(app)
