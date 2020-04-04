import tweepy
import time

auth = tweepy.OAuthHandler('*************************', '**************************************************')
auth.set_access_token('**************************************************', '*********************************************')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

search_string = 'python'
numberoftweets = 2

for tweets in tweepy.Cursor(api.search, search_string).items(numberoftweets):
    try:
        tweets.favourite()
        print('Good tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration
        break
