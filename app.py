import json
from flask import Flask

app = Flask(__name__)

post1 = {
    "title" : "Good day",
    "content": "Today I met a girl. She had black eyes and loves ice-cream"
}

post2 = {
    "title": "Bad day",
    "content": "Today, she did show up and I felt more lonely than ever"
}

print(post1["title"])
print(post1["content"])

posts = [post1, post2]

@app.route('/')
def main():
    return json.dumps(posts)


if __name__ == '__main__':
    app.run()
