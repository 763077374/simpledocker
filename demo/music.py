import web
urls = (
    '/','Index',
    '/s', 'So'
)
app = web.application(urls, globals())
render = web.template.render('templates')
class Index:
    def GET(self):
        i = web.input()
        name = i.get('name')
        mp3info = getmp3url(name)
        mp3url,mp3pic = mp3info
        return mp3info
class So:
    def GET(self):
        return 's ok'
class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'
import urllib
import json
def getmp3url(name):
    url = 'https://s.music.163.com/search/get/?type=1&s=%s&limit=1'%name

    html=urllib.urlopen(url)
    text = json.load(html)
    text = text["result"]["songs"][0]
    mp3url = text["audio"]
    mp3img = text["album"]["picUrl"]

    return mp3url,mp3img
if __name__ == "__main__":
    app.run()

