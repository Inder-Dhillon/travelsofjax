import tweepy
from tweepy import Stream
from tweepy import StreamListener
from PIL import Image
import requests
import random
from io import BytesIO

CONSUMER_KEY = "LCufTOKIRHPPsuRMDJCH6teGs"
CONSUMER_SECRET = "Z4hlsN4w1w1zBL1ckutNblajYT19utl1eMliPv0k6c8PvkZUba"
ACCESS_KEY = "1110638074558595073-YxPezECSCdkIkmKc6vbGzECPFVueDe"
ACCESS_SECRET = "B3tPZ9C24tSf8Eq4x5qyt8UYgMdtEYVNsAglSUArICEMp"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def new_landscape():
    jax = Image.open('jax.png')
    url = 'https://www.reddit.com/r/EarthPorn.json?limit=100'
    response = requests.get(url, headers={'User-agent': 'Jaxson 0.1'})
    if not response.ok:
        print("Error", response.status_code)
        exit()
    data = response.json()['data']['children']
    first_post = data[random.randint(1, 101)]['data']
    image_url = first_post['url']
    if '.png' in image_url:
        extension = '.png'
    elif '.jpg' in image_url or '.jpeg' in image_url:
        extension = '.jpeg'
    else:
        image_url += '.jpeg'
        extension = '.jpeg'
    # prevents thumbnails denoting removed images from being downloaded
    image = requests.get(image_url, allow_redirects=False)
    if (image.status_code == 200):
        img = Image.open(BytesIO(image.content))

        basewidth = int(img.width / 3.7)
        wpercent = (basewidth / float(jax.size[0]))
        hsize = int((float(jax.size[1]) * float(wpercent)))
        jax = jax.resize((basewidth, hsize), Image.ANTIALIAS)
        img.paste(jax, (random.randint(0, img.width - 300), random.randint(0, img.height - 300)), jax)
        img.save('temp.jpeg')

class StdOutListener(StreamListener):
    def on_status(self, status):
        if 'RT' not in status.text:
            print('Tweet text: ' + status.text)
            s = status.author.screen_name
            print(s)
            api.create_favorite(status.id)
            try:
                api.retweet(status.id)
                message = 'Hey @' + s + ' I am currently here!'
                new_landscape()
                api.update_with_media(filename='temp.jpeg',status=message, in_reply_to_status_id=status.id)
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
