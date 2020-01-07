# Jaxson - The Twitter Bot <img src='https://www.inderdhillon.com/files/logo-gray.png' width=100 align='right'>
>Inder Dhillon <br>
>inderdhillon.com <br>

### Description:
Using Twitter API and Reddit API to stick an image of my friend's cat on a random landscape from Reddit and replying the image to anyone who uses the hashtag #jaxsonreplies on Twitter.

### Overview:
The program pulls a random landscape from a subreddit on Reddit using Reddit's API to get a json file. Then it uses pillow library to overlay my friend's cat on the landscape. Then it uses Twitter API's streaming endpoint to listen for any tweets with the hashtag #jaxsonreplies and replies with the image formed using pillow. 

##### Modules used:
tweepy : Twitter's API Wrapper <br>
pillow : Image manipulation <br>
requests : Getting json data
random : Selecting random image from a subreddit

##### Example:
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hey <a href="https://twitter.com/inderdhillxn?ref_src=twsrc%5Etfw">@inderdhillxn</a> I am currently here! <a href="https://t.co/lnEpbVtuqM">pic.twitter.com/lnEpbVtuqM</a></p>&mdash; Jaxson (@JaxsonReplies) <a href="https://twitter.com/JaxsonReplies/status/1214658259069624320?ref_src=twsrc%5Etfw">January 7, 2020</a></blockquote>
