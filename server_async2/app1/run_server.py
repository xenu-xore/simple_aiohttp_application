from server_async2.app1 import web, make_app

web.run_app(make_app(), host="localhost", port=80)