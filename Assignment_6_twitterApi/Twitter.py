import sys
import json
import requests
from requests_oauthlib import OAuth1


class Twitter:
    def __init__(self, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET):
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET = CONSUMER_SECRET

    def getUrl(self, username, tweet_field='created_at', expansions='author_id', user_field='', max_tweets=10):
        self.username = username
        self.tweet_field = tweet_field
        self.expansions = expansions
        self.user_field = user_field
        self.max_tweets = max_tweets

        username = "username={}".format(username)
        user_field = "user.fields={}".format(user_field)
        tweet_field = "tweet.fields={}".format(tweet_field)
        expansions = "expansions={}".format(expansions)

        url = "https://api.twitter.com/2/users/{}/{}&{}&{}&max_results={}".format(username, tweet_field, expansions,
                                                                                   user_field, max_tweets)
        return url
    def tweetApi(self,url):
        """
        username = "username={}".format(self.username)
        user_fields = "user_fields"

        self.url = "https://api.twitter.com/2/users/{}/{}".format(username, user_fields)"""

        response = requests.request("GET", url,
                                    auth=OAuth1(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET, self.CONSUMER_KEY,
                                                self.CONSUMER_SECRET))
       # print(response.json())
        print(response)
        return response.json()

    def streamTweets(self):
        tweet_url = self.getUrl(self.username, self.tweet_field, self.expansions, self.user_field, self.max_tweets)
        json_dict = self.tweetApi(tweet_url)
        print(json_dict)
        dic=json.loads(json.dumps(json_dict,sort_keys=True))
        return

    def getTweets(self, tweet_data):
        self.tweet_data = tweet_data
        tweet_data_json = self.streamTweets()
        ''''''
        for i in range(len(tweet_data_json['data'])):
            if x in tweet_data_json['data'][i].keys():
                if x =="author_id":
                    tweet_data.append([tweet_data_json['data'][i][x]])
                elif x =="public_metrics":
                    tweet_data[i+1].append(tweet_data_json['data'][i][x]['like_count'])
                    tweet_data[i+1].append(tweet_data_json['data'][i][x]['retweet_count'])
                else:
                    tweet_data[i+1].append(tweet_data_json['data'][i][x])

