# dog-rates

Plots the distribution of the ratings of [@dog_rates](https://twitter.com/dog_rates/) (aka WeRateDogs™) over time.

I used twitter's advanced search to obtain more than 3200 tweets (the maximum number of tweets obtainable through the api). Unfornately some tweets are still missing, as that search was unable to retrieve them all. It still gives a decent idea of how the given ratings change over time. I did not get new tweets after 2019-01-01 in order to have a non random stopping point. Ratings were not included if they were not out of ten, contained more than two digits (ex. 420/10 and 1776/10 were present), or if it was not an integer.

Run get_tweets.py first, then create_frames.py. The resulting frames were used to create a video with ffmpeg. This was the command I used.

```
sudo ffmpeg -f image2 -r 48 -i ~/DogRateFrames/frame%03d.png -vcodec mpeg4 -y dog_rates.mp4
```
