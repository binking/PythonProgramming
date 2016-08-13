import tweepy
from tweepy import OAuthHandler

api_key = "B1uB90Z0CpcaFmzkeJ9NHqOYh"
api_secret = "2eCI6Y3pPwt3ObPBYpru08VvWgJndLqQx7Y96i3EYt5O551Lid"
access_token_key = "4567647824-zUOChj4BWkDNia3Rd0fIgrHbLGnM0rai1C2ITzy"
access_token_secret = "HQhI0oVRymS5dr1waI3Fnr3GK7hsrsFU2li12q7ORmaUb"

auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token_key, access_token_secret)
twiterAPI = tweepy.API(auth)

for status in tweepy.Cursor(twiterAPI.home_timeline).items(10):
    print(status.text)

for resultset in  tweepy.Cursor(twiterAPI.home_timeline).pages(3):
    for result in resultset:
        print(result.text)