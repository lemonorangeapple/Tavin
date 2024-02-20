import webview
from flask import *
import os
import sys
os.chdir(sys._MEIPASS if sys._MEIPASS else os.path.abspath("."))

class Tavin:
    def __init__(self, env):
        self.app = Flask(env)
        self.api = webview_api()
        self.window = webview.create_window(url = self.app)

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