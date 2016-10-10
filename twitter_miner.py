# EXAMPLE USAGE: python twitter_miner.py 'test.csv' \#hillary \#trump
# This will monitor hashtags with #hillary and #trump and save tweets to test.csv
# Uses a twitter app API key for generic twitter mining.
# Note that if you want to mine hashtags, you have to use \ to escape the # in the command line

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import csv
import sys

#Variables that contains the user credentials to access Twitter API
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

class StdOutListener(StreamListener):

    def __init__(self, api = None):
        self.api = api
        filename = sys.argv[1]
        csvFile = open(filename, 'w')

    def on_status(self, status):

        filename = sys.argv[1]
        csvFile = open(filename, 'a')

        csvWriter = csv.writer(csvFile)

        if not 'RT @' in status.text:
            try:
                csvWriter.writerow([status.text,
                                    status.created_at,
                                    status.geo,
                                    status.lang,
                                    status.place,
                                    status.coordinates,
                                    status.user.favourites_count,
                                    status.user.statuses_count,
                                    status.user.description,
                                    status.user.location,
                                    status.user.id,
                                    status.user.created_at,
                                    status.user.verified,
                                    status.user.following,
                                    status.user.url,
                                    status.user.listed_count,
                                    status.user.followers_count,
                                    status.user.default_profile_image,
                                    status.user.utc_offset,
                                    status.user.friends_count,
                                    status.user.default_profile,
                                    status.user.name,
                                    status.user.lang,
                                    status.user.screen_name,
                                    status.user.geo_enabled,
                                    status.user.profile_background_color,
                                    status.user.profile_image_url,
                                    status.user.time_zone,
                                    status.id,
                                    status.favorite_count,
                                    status.retweeted,
                                    status.source,
                                    status.favorited,
                                    status.retweet_count])
            except Exception as e:
                print(e)
                pass

        csvFile.close()

        return

    def on_error(self, status_code):
        print('Encountered error with status code:', status_code)
        return # Don't kill the stream

    def on_delete(self, status_id, user_id):
        """Called when a delete notice arrives for a status"""
        print("Delete notice")
        return

    def on_limit(self, track):
        # If too many posts match our filter criteria and only a subset is sent to us
        print("!!! Limitation notice received")
        return True

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        time.sleep(10)
        return True

l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)

#This line filter Twitter Streams to capture data by the keywords
stream.filter(track=sys.argv[2:])
