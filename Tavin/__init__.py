import webview
from flask import *

class Tavin:
    def __init__(self, title, env, **args):
        self.app = Flask(env)
        self.window = webview.create_window(url = self.app, title = title, **args)
        self.route = self.app.route

    def get_app(self):
        return self.app

    def run(self):
        webview.start()