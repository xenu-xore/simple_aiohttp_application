from server_async2.app1 import web
import aiohttp_jinja2
from aiohttp_session import get_session
import time

web_app1 = web.RouteTableDef()


@web_app1.get('/', name="home")
@aiohttp_jinja2.template('home.html')
async def get_handler(request):

    location_login = request.app.router["do_login"].url_for()

    session = await get_session(request)
    session['rabotaem'] = time.time()

    return {"location_login": location_login}


@web_app1.get('/page', name='page_test')
@aiohttp_jinja2.template('page.html')
async def page(request):
    return {}
