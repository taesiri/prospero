from app import app
from flask import render_template
import json

@app.route('/')
@app.route('/index')
def index():

    # Loading data
    engadget_posts = {}
    with open('app/data/engadet.json') as f:
      engadget_posts = json.load(f)

    all_tweets = list(open('app/data/twitter.json'))
    tweets = [json.loads(t) for t in all_tweets]

    # Returning the view, filled with data!
    return render_template('index.html', title='Prospero News!', posts=engadget_posts, tweets=tweets)
