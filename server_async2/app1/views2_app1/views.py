from server_async2.app1 import web
import aiohttp_jinja2
from aiohttp_session import get_session, new_session

web_app2 = web.RouteTableDef()


@web_app2.get('/login', name='do_login')
@web_app2.post('/login', name='do_login')
@aiohttp_jinja2.template('login.html')
async def do_login(request):
    if request.method == 'POST':
        form = await request.post()
        if form['login'] == 'admin' and form['password'] == "admin":
            session = await new_session(request)

            session['login'] = form['login']
            session['password'] = form['password']
            location = request.app.router["page_test"].url_for()
            raise web.HTTPFound(location=location)
        else:
            return {'error': "Неверный логин/пароль"}

@web_app2.get('/json')
async def get_handler(request):
    return web.json_response({'app': 'Это асинхронное приложение 2'})


