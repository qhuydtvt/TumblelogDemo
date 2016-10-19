import json
from flask import Flask, request

app = Flask(__name__)


posts = []

@app.route('/')
def main():
    return json.dumps(posts)

@app.route('/addpost', methods=["POST"])
def add_post():
    args = request.form
    title_value = args["title"]
    content_value = args["content"]
    new_post = {
        "title" : title_value,
        "content" : content_value
    }
    posts.append(new_post)
    print(title_value, content_value)
    return "OK"

if __name__ == '__main__':
    global posts
    post1 = {
        "title": "Good day",
        "content": "Today I met a girl. She had black eyes and loves ice-cream"
    }

    post2 = {
        "title": "Bad day",
        "content": "Today, she did show up and I felt more lonely than ever"
    }

    print(post1["title"])
    print(post1["content"])
    app.run()
