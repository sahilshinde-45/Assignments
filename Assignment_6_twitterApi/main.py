import string

from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import Parse
from decouple import config
import numpy as np
import pandas as pd
import Pdf

# # # # TWITTER CLIENT # # # #
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client


# # # # TWITTER AUTHENTICATER # # # #
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(config('CONSUMER_KEY'), config('CONSUMER_SECRET'))
        auth.set_access_token(config('ACCESS_TOKEN'), config('ACCESS_TOKEN_SECRET'))
        return auth


# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self):
        self.twitter_autenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_autenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class TwitterListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            # Returning False on_data method in case rate limit occurs.
            return False
        print(status)  # will print out the status message of the error


class TweetAnalyzer:
    """
    Functionality for analyzing and categorizing content from tweets.
    """

    def clean_csv_twitterFile(self):
        fileParseObj = Parse.Parse('tweets.csv')

        data = fileParseObj.csv_reader()
        print(data)
        for i in data:
            i[1] = i[1].encode('latin-1', 'replace').decode('latin-1')
            i[1] = str(i[1]).translate(str(i[1]).maketrans('', '', string.punctuation))

            print(i)
            print(data)
        self.header = fileParseObj.fetchHeader()

        self.value = fileParseObj.fetchValue()
        parse = fileParseObj.write(self.header,self.value)
        for item in data:
            # print(item)
            parse.writerow(item)



    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

        df['id'] = np.array([tweet.id for tweet in tweets])
        df['len'] = np.array([len(tweet.text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])

        return df


if __name__ == '__main__':
    """
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    api = twitter_client.get_twitter_client_api()

    tweets = api.user_timeline(screen_name="UNFCCC", count=20)

    # print(dir(tweets[0]))
    # print(tweets[0].retweet_count)

 
    df = tweet_analyzer.tweets_to_data_frame(tweets)

    # print(df.head(10))

    dataset = df.head(10)
    #print(dataset)

    dataset.to_csv('tweets.csv')
"""
    df = pd.read_csv('tweets.csv')
    df.shape  # Return a tuple representing the dimensionality of the DataFrame.

    TweetAnalyzer.clean_csv_twitterFile("tweets.csv")

