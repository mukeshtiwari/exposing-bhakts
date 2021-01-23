import tweepy
from keys import keys #keep keys in separate file, keys.py

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']

try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    fol = tweepy.Cursor(api.followers, id = 'mukesh_tiwari')

    for page in fol.pages():
      print(page) 

except Exception as e:
    print(e)

