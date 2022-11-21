
from unicodedata import name
from sanic import Sanic
from sanic.response import text
from sanic.response import json
from sanic.response import html
from blueprints.city_data import bp
from sanic_ext import Extend

app = Sanic("MyHelloWorldApp")
Extend(app)
app.blueprint(bp)
app.static('/static', './static')
#app.run(host='0.0.0.0', port=1337, access_log=False)

""" @app.get("/")
async def hello_world(request):
    #print(request.files.get("asd").body)
    return json({"home":"Chaged this"})

@app.get('/test')
async def test(request):
    print(request)
    return text('Changed')

@app.get('/html')
async def test(request):
    #print(request)
    return html('<!DOCTYPE html><html lang="en"><meta charset="UTF-8"><div>Hi 😎 some html response</div>') """