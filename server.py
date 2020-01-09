from os import environ
from flask import Flask

app = Flask(__name__)
app.run(host= '0.0.0.0', port=environ.get('PORT'))

import praw

reddit = praw.Reddit(client_id=environ['REDDIT_ID'],
                     client_secret=environ['REDDIT_SECRET'],
                     password=environ['REDDIT_PASSWORD'],
                     user_agent='imdad',
                     username='imdad_bot')
subreddit = reddit.subreddit("all")  # subreddits

for comment in subreddit.stream.comments():
    comment_lower = comment.body.lower()
    comment_lower_list = comment_lower.split(" ")
    try:
        if "im" in comment_lower_list:
            comment.reply("Hi " + comment_lower_list[comment_lower_list.index("im") + 1].replace(",","") + ", I'm Dad👨")
        elif "i'm" in comment_lower_list:
            comment.reply("Hi " + comment_lower_list[comment_lower_list.index("i'm") + 1].replace(",","") + ", I'm Dad👨")
    except:
        pass