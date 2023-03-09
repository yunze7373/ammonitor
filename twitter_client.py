import tweepy

class TwitterClient:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        auth = tweepy.OAuth1UserHandler(
            api_key, api_secret_key, access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def send_tweet(self, message):
        self.api.update_status(message)
