import os
import tweepy
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get credentials from environment variables
consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_SECRET")

# Authenticate with Twitter API using Tweepy
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
twitter_client = tweepy.API(auth)

# Example function to post a tweet
def post_tweet(message: str):
    try:
        twitter_client.update_status(status=message)
        return {"status": "success", "message": "Tweet posted successfully!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
