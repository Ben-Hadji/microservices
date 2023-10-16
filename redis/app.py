from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='localhost', port=6379)

@app.route('/')
def visit_counter():
    redis.incr('page_visits')
    visits = redis.get('page_visits').decode('utf-8')
    return f'This is a counter web page. It has been visited {visits} times.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
