from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

consumer_key = 'oggx94jMpnAL3P0qAp7jRRCNr'
consumer_secret = 'wgnUKMwmVNqxrYqEvSdEc2xl7fW0CphpoSKgGGrAJok7e3iw02'
access_token = '1295930741449089024-QONEtvz7YQ1Fj5EwlF0JkXakNUaXVP'
access_secret = 'k42vlXE2chunIHpNXZdJu3PS8KFygSi0wHt7CZhg5Zr6Y'

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
    	fname = sys.argv[1]
    	try:
    		with open(fname, 'a') as f:
    			f.write(data)
    			return True
    	except BaseException as e:
    		print("Error in writing to file")
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    stream = Stream(auth, l)
stream.filter(track=['Aquaman'])
