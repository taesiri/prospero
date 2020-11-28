from app import app
from flask import render_template
import json
import random

@app.route('/')
@app.route('/index')
def index():

    # Loading data
    engadget_posts = {}
    with open('app/data/engadget.json') as f:
      engadget_posts = json.load(f)

    # fake id for Modals - This is just a hacky way to show multiple modals with different data
    # the proper way is through JS, but I chose this way at this stage.
    random_ids = random.sample(range(1, 100), len(engadget_posts))
    for i, post in enumerate(engadget_posts):
      post['modalid'] = random_ids[i]

    all_tweets = list(open('app/data/twitter.json'))
    tweets = [json.loads(t) for t in all_tweets]

    # Returning the view, filled with data!
    return render_template('index.html', title='Prospero News!', posts=engadget_posts, tweets=tweets)
