# Tavin

一个简洁而不简单的应用框架。
> A concise yet not simple application framework.

使用方式：
> Usage:

```python
from Tavin import *

app = Tavin(title = "Tavin")

def index():
    return '123'

app.add_url_rule('/', index)

app.run()
```