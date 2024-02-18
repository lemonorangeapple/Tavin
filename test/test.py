from Tavin import *
app = Tavin(title = "Tavin", env = __name__)

@app.route('/')
def index():
    return "index"

@app.route('/return_text')
def return_text():
    return "hello world"

@app.route('/return_template')
def return_template():
    return render_template('index.html')

@app.route('/return_file')
def return_file():
    with open('index.txt', 'r', encoding = 'utf-8') as f:
        return f.read()

@app.route('/return_redirect')
def return_redirect():
    return redirect('/')

app.run()