import os
os.system('python -m pip install aiohttp')
from aiohttp import web
app = web.Application()

routes = web.RouteTableDef()

@routes.get('/')
async def main(req):
    return web.Response(text='e')

app.add_routes(routes)
web.run_app(app)
