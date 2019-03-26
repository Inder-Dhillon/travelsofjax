import time
import sys
import tweepy
from os import environ
from tweepy import Stream
from tweepy import StreamListener

CONSUMER_KEY = "LCufTOKIRHPPsuRMDJCH6teGs"
CONSUMER_SECRET = "Z4hlsN4w1w1zBL1ckutNblajYT19utl1eMliPv0k6c8PvkZUba"
ACCESS_KEY = "1110638074558595073-YxPezECSCdkIkmKc6vbGzECPFVueDe"
ACCESS_SECRET = "B3tPZ9C24tSf8Eq4x5qyt8UYgMdtEYVNsAglSUArICEMp"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class StdOutListener(StreamListener):

    def on_status(self, status):
        if 'RT' not in status.text:
            print('Tweet text: ' + status.text)
            s = status.author.screen_name
            print(s)
            api.create_favorite(status.id)
            try:
                api.retweet(status.id)
                message = '@' + s + ' You tweeted with my hashtag!'
                api.update_status(status=message, in_reply_to_status_id=status.id)
            except:
                try:
                    print('duplicate tweet error')
                    message = '@' + s + ' You tweeted with my hashtag AGAIN!'
                    api.update_status(status=message, in_reply_to_status_id=status.id)
                except:
                    print('double duplicate tweet error')
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True  # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True  # To continue listening


if __name__ == '__main__':
    listener = StdOutListener()

    stream = Stream(auth, listener)
    stream.filter(track=['#jaxson'])
