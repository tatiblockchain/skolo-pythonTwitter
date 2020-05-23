import config
import tweepy
import time
import requests
import json
import testing


url_total = "https://covid-api.com/api/reports/total"
url_regions = "https://covid-api.com/api/regions"
#Replace ISO code with your Country
url_specific = "https://covid-api.com/api/reports?iso=ZAF"

access_token = "enter your access token here"
access_secret = "enter your access secret here"

api_key = "enter your api key here"
api_secret = "enter your api secret here"


auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.access_secret)
api = tweepy.API(auth)

def localCovidPosts():
    #Get the Global Total Numbers
    r = requests.get(url_specific)
    results = json.loads(r.text)

    last_update = results['data'][0]['last_update']
    confirmed = str(results['data'][0]['confirmed'])
    deaths = str(results['data'][0]['deaths'])
    recovered = str(results['data'][0]['recovered'])


    tweet_string = "Latest confirmed COVID numbers in South Africa are {}, deaths {} and recovered {}. Last updated {}".format(confirmed, deaths, recovered, last_update)


    api.update_status(tweet_string)
    print("Tweet sent succesfully")


def globalCovidPosts():
    #Get the Global Total Numbers
    r = requests.get(url_total)
    results = json.loads(r.text)

    last_update = results['data']['last_update']
    confirmed = str(results['data']['confirmed'])
    deaths = str(results['data']['deaths'])
    recovered = str(results['data']['recovered'])

    tweet_string = "The latest confirmed covid numbers globally are {}, deaths {} and recovered {}. Last updated {}".format(confirmed, deaths, recovered, last_update)


    api.update_status(tweet_string)
    print("tweet sent succesfully")



while True:
    globalCovidPosts()
    time.sleep(42000)
    testing.randomTextRandomImage()
    time.sleep(42000)
