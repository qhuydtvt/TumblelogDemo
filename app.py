from mongoengine import *
from mlab import *
import json
from flask import *

app = Flask(__name__)

class Post(Document):
    title = StringField()
    content = StringField()
    def get_json(self):
        return {"title": self.title, "content": self.content}

@app.route('/')
def main():
    posts = Post.objects
    return jsonify([post.get_json() for post in posts])

@app.route('/addpost', methods=["POST"])
def add_post():
    args = request.form
    title_value = args["title"]
    content_value = args["content"]
    p = Post(title=title_value, content=content_value)
    p.save()
    return jsonify({"code": 1, "message": "OK"})

if __name__ == '__main__':
    mlab_connect()
    app.run()
