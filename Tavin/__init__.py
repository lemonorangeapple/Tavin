import webview
from flask import Flask, render_template

class webview_api:
    def __init__(self):
        self._window = None

    def set_window(self, window):
        self._window = window

    def quit(self):
        self._window.destroy()

class Tavin:
    def __init__(self, **args):
        self.app = Flask(__name__)
        self.api = webview_api()
        self.window = webview.create_window(url = self.app, js_api = self.api, **args)

    def get_app(self):
        return self.app

    def add_url_rule(self, path, route):
        self.app.add_url_rule(path, path, route)

    def run(self):
        self.api.set_window(self.window)
        webview.start()
    