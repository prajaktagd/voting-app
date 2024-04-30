from flask import Flask, make_response, render_template, request, g
from redis import Redis
import json
import random

app = Flask(__name__)

def get_redis():
    if not hasattr(g, 'redis'):
        g.redis = Redis(host="redis", db=0, socket_timeout=5)
    return g.redis

@app.route("/", methods=["GET", "POST"])
def hello_world():
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]
    
    vote = None

    if request.method == 'POST':
        redis = get_redis()
        vote = request.form['vote']
        data = json.dumps({'voter_id': voter_id, 'vote': vote})
        redis.rpush('votes', data)

    response = make_response(render_template(
        'index.html',
        option_a="Cats",
        option_b="Dogs",
        vote=vote
    ))
    
    response.set_cookie('voter_id', voter_id)
    return response

if(__name__ == "__main__"):
    app.run(host="0.0.0.0" ,port=80)