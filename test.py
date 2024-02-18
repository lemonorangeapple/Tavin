from Tavin import *
app = Tavin(title = "Tavin", env = __name__, width = 800, height = 600)

@app.route('/')
def index():
    return render_template('index.html')

app.run()