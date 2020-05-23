import config
import tweepy
import random
import time

num = 1 + 1

def randomStringPost():
    access_token = "enter your access token here"
    access_secret = "enter your access secret here"

    api_key = "enter your api key here"
    api_secret = "enter your api secret here"


    auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)


    st1 = "This is the day you get your amaxing nail set - shop now"
    st2 = "find us at https://thetatistore.com today"
    st3 = "Stay at home and Do your own nails - woop woop"
    st4 = "Lockdown discount available in store >>> https://thetatistore.com"
    st5 = "There is no better time than the present to start shopping for a bargain"
    st6 = "The leading nail suppliers this side of the world - come visit us soon"


    hashtags = ["#OnlineShopping", "#COVIDSale", "#SouthAfrica", "#SALE", "#salesalesale", "#Bargain", "#nails", "#nailsalon", "#polygel", "#NailsOfInstagram", "#polygelnails"]
    tweet_strings = [st1, st2, st3, st4, st5, st6]
    random_string = random.choice(tweet_strings)

    selected_tweet = random_string + " " + random.choice(hashtags) + " " + random.choice(hashtags) + " " + random.choice(hashtags)  + " "+ random.choice(hashtags)

    if (len(selected_tweet) > 140):
        time.sleep(1)
        pass
    else:
        api.update_status(selected_tweet)
        print("SUCCESS --- good to go")


def randomImagePost():
    access_token = "enter your access token here"
    access_secret = "enter your access secret here"

    api_key = "enter your api key here"
    api_secret = "enter your api secret here"


    auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)


    image1 = "day1Other.jpg"
    image2 = "day2Other.jpg"
    image3 = "day3Other.jpg"
    image4 = "day4Other.jpg"
    image5 = "day7Other.jpg"
    image6 = "day8Other.jpg"
    image7 = "day9Other.jpg"
    image8 = "day10Other.jpg"
    images = [image1, image2, image3, image4, image5, image6, image7]
    selected_image = random.choice(images)

    api.update_with_media(selected_image)
    print("Image posted succesfully")

def randomTextRandomImage():
    access_token = "enter your access token here"
    access_secret = "enter your access secret here"

    api_key = "enter your api key here"
    api_secret = "enter your api secret here"


    auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)

    image1 = "day1Other.jpg"
    image2 = "day2Other.jpg"
    image3 = "day3Other.jpg"
    image4 = "day4Other.jpg"
    image5 = "day7Other.jpg"
    image6 = "day8Other.jpg"
    image7 = "day9Other.jpg"
    image8 = "day10Other.jpg"
    images = [image1, image2, image3, image4, image5, image6, image7]
    selected_image = random.choice(images)



    st1 = "This is the day you get your amaxing nail set - shop now"
    st2 = "find us at https://thetatistore.com today"
    st3 = "Stay at home and Do your own nails - woop woop"
    st4 = "Lockdown discount available in store >>> https://thetatistore.com"
    st5 = "There is no better time than the present to start shopping for a bargain"
    st6 = "The leading nail suppliers this side of the world - come visit us soon"
    hashtags = ["#OnlineShopping", "#COVIDSale", "#SouthAfrica", "#SALE", "#salesalesale", "#Bargain", "#nails", "#nailsalon", "#polygel", "#NailsOfInstagram", "#polygelnails"]
    tweet_strings = [st1, st2, st3, st4, st5, st6]
    random_string = random.choice(tweet_strings)
    selected_tweet = random_string + " " + random.choice(hashtags) + " " + random.choice(hashtags) + " " + random.choice(hashtags)  + " "+ random.choice(hashtags)

    if (len(selected_tweet) > 140):
        time.sleep(1)
        pass
    else:
        api.update_with_media(selected_image, selected_tweet)
        print("{} with Image posted Succesfull".format(selected_tweet))
        print("SUCCESS --- good to go")
