import tweepy
import time

auth = tweepy.OAuthHandler('x8d96c5QiGfC5uWkuqXsogiam', 'ZxEStKAeb0XDUvLRIhba8yPX0zXMOdIQlykZGh0rcq8LQsb3oF')
auth.set_access_token('1243219581143040001-Unj48Tn5tEvonBHPFOWOL5BXlgzlpM', 'WawL3Yy4cSkhgJsD1hy18TeIy2HO0dZ4kQfKCzZhyLSgm')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.follow_count > 100:
        follower.follow()