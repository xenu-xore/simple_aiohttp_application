from server_async2.app1 import web
import aiohttp_jinja2
from aiohttp_session import get_session, new_session

web_app1 = web.RouteTableDef()


@web_app1.get('/', name="home")
@aiohttp_jinja2.template('home.html')
async def get_handler(request):
    location_login = request.app.router["do_login"].url_for()

    session = await get_session(request)
    return {'url_login': location_login, 'session_login': session}


@web_app1.get('/page', name='page_test')
@aiohttp_jinja2.template('page.html')
async def page(request):
    return {}
