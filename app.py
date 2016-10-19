from mongoengine import *
from mlab import *
import json
from flask import *

app = Flask(__name__)
mlab_connect()

class Post(Document):
    title = StringField()
    content = StringField()
    def get_json(self):
        return {"title": self.title, "content": self.content}

@app.route('/')
def main():
    return jsonify([post.get_json() for post in Post.objects])

@app.route('/addpost', methods=["POST"])
def add_post():
    args = request.form
    title_value = args["title"]
    content_value = args["content"]
    p = Post(title=title_value, content=content_value)
    p.save()
    return jsonify({"code": 1, "message": "OK"})

if __name__ == '__main__':
    app.run()
