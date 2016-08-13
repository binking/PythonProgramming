import tweepy
from tweepy import OAuthHandler

consumer_key = "B1uB90Z0CpcaFmzkeJ9NHqOYh"
consumer_secret = "2eCI6Y3pPwt3ObPBYpru08VvWgJndLqQx7Y96i3EYt5O551Lid"
access_token_key = "4567647824-zUOChj4BWkDNia3Rd0fIgrHbLGnM0rai1C2ITzy"
access_token_secret = "HQhI0oVRymS5dr1waI3Fnr3GK7hsrsFU2li12q7ORmaUb"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)
