from bottle import route, run, static_file, template
import feedparser
import ssl
import json
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

feed = feedparser.parse('https://www.jpost.com/Rss/RssFeedsHeadlines.aspx')

@route('/get_all', method='GET')
def feed_info():
    list_of_posts = []
    for i in range(len(feed["entries"])):
        post = {
            "title": feed["entries"][i]["title"],
            "link": feed["entries"][i]["link"]
        }
        list_of_posts.append(post)
    return json.dumps(list_of_posts)


@route('/', method='GET')
def get_app():
    return template("index.html")

@route('/css/<filename:re:.*\.css>' , method='GET')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@route('/img/<filename:re:.*\.(jpg|png)>', method='GET')
def img(filename):
    return static_file(filename, root='static/img')

@route('/js/<filename:re:.*\.js>', method='GET')
def js(filename):
    return static_file(filename, root='static/js')


def main():
        run(host='localhost', port=7000)


if __name__ == '__main__':
        main()
