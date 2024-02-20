import webview
from flask import *

class webview_api:
    def __init__(self) -> None:
        self._window = None
    def set_window(self, window):
        self._window = window
    def quit(self):
        self._window.destroy()

class Tavin:
    def __init__(self, title, env, **args):
        self.app = Flask(env)
        self.api = webview_api
        self.window = webview.create_window(url = self.app, title = title, js_api = webview_api, **args)

    def get_app(self):
        return self.app

    def _route(self, route):
        path = self.path
        self.app.add_url_rule(path, path, route)
        self.path = ''

    def route(self, path):
        self.path = path
        return self._route

    def run(self):
        self.api.set_window(self.window)
        webview.start()