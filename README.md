# Tavin

一个简洁而不简单的应用框架。
> A concise yet not simple application framework.

使用方式：
> Usage:

```python
from Tavin import *

app = Tavin(title = "Tavin", env = __name__, width = 800, height = 600)

@app.route('/')
def index():
    return render_template('index.html')

app.run()
```