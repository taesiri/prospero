# simple Twint-based crawler to get PS5 tweets
import twint

# Create a (defualt) Config
c = twint.Config()

# options are self explanatory
c.Search = 'PS5'
c.Limit = 25
c.Lang = "en"
c.Min_likes = 25 # let's get tweets with at least 25 likes
c.Store_json = True
c.Output = "tweets.json"

# Run the search
twint.run.Search(c)