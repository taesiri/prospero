from wordcloud import WordCloud, STOPWORDS 
from bs4 import BeautifulSoup
import json
import matplotlib 
import matplotlib.pyplot as plt
import re

# List of StopWords to exlude from WC
stopwords = set(STOPWORDS) 

def generate_engadget_wc():
  # Load all Engadget posts
  engadget_posts = []
  with open('../Server/app/data/engadget.json', 'r') as f:
    engadget_posts = json.load(f)

  # Generate One big text variable that contains all posts 
  engadget_all_texts = ''

  for p in engadget_posts:
    # Posts['body'] contains actual html, to convert it to text, we also use BS here
    article = '\n'.join([BeautifulSoup(paragraph, 'html.parser').text for paragraph in p['body']])
    engadget_all_texts += article 

  # Generating Word Cloud
  eng_cloud = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stopwords, min_font_size = 10).generate(engadget_all_texts)
  return eng_cloud


def generate_twitter_wc():
  # load tweets
  all_tweets = list(open('../Server/app/data/twitter.json'))
  tweets = [json.loads(t) for t in all_tweets]
  tweets = [t['tweet'] for t in tweets]
  
  # Generate one string containing all tweets
  all_tweets_texts  = '\n'.join(tweets)
  # Remove Links using Regex
  all_tweets_texts  = re.sub(r"http\S+", "", all_tweets_texts)

  # Generating Word Cloud
  tweetcloud = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stopwords, min_font_size = 10).generate(all_tweets_texts)
  return tweetcloud


engadget_cloud = generate_engadget_wc()
tweet_cloud    = generate_twitter_wc()


# Plotting

fig, axes = plt.subplots(1, 2, figsize=(24,12))
axes[0].imshow(engadget_cloud)
axes[1].imshow(tweet_cloud)

for ax in axes:
  ax.grid(None)
  ax.axis("off")

axes[0].set_title('engadget', fontdict={'fontsize': 21, 'fontweight': 'medium'}, y= 1.01)
axes[1].set_title('twitter', fontdict={'fontsize': 21, 'fontweight': 'medium'}, y= 1.01)

fig.suptitle('Word Cloud', fontsize=26, y=1.06)
line = plt.Line2D([0.5,0.5],[0, 1], transform=fig.transFigure, color="black", linewidth=3)
fig.add_artist(line)
plt.tight_layout(pad = 0)
plt.savefig('wordcloud.png', bbox_inches='tight')
plt.show()