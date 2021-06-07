import jinja2
import os
import aiohttp_jinja2
import base64
from cryptography import fernet
from aiohttp import web
from aiohttp_session import setup, get_session, session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")

from views2_app1.views import web_app2
from views_app1.views import web_app1


async def make_app():
    app = web.Application()

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATE_PATH))


    # secret_key must be 32 url-safe base64-encoded bytes
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))
    app.add_routes(web_app1)
    app.add_routes(web_app2)
    return app







