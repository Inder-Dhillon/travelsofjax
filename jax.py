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

