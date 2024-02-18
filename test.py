from Tavin import *
app = Tavin(title = "Tavin", width = 800, height = 600)

def index():
    return '123'
app.add_url_rule('/', index)

app.run()