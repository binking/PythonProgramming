import json, sys

def getPlaceField(tweets, field):
    # Pick American tweets
    placeFields = {}; i=0
    for tweet in tweets:
        tweet = json.loads(tweet)
        try :
            if tweet[field]:
                i += 1
                print i, field.capitalize(), tweet[field]
        except KeyError:
            pass

def getLocationField(tweets):
    # Pick American tweets
    placeFields = {}; i = 0
    for tweet in tweets:
        tweet = json.loads(tweet)
        try :
            if tweet['user']['location']:
                i += 1
                print i, 'User\' location : ', tweet['user']['location']
        except KeyError:
            pass        
def main():
    tweet_file = open(sys.argv[1], 'r')
    tweets = tweet_file.readlines()
    #getPlaceField(tweets, 'place')
    #getPlaceField(tweets, 'coordinates')
    #getPlaceField(tweets, 'geo')
    getLocationField(tweets)
    
if __name__=="__main__":
    main()

'''
place field :
{u'full_name': u'Vi\xf1a del Mar, Valpara\xedso', u'url': u'https://api.twitter.com/1.1/geo/id/008be613029d4ca5.json', u'country': u'Chile', u'place_type': u'city', u'bounding_box': {u'type': u'Polygon', u'coordinates': [[[-71.5898331, -33.1045519], [-71.5898331, -32.9481633], [-71.4414593, -32.9481633], [-71.4414593, -33.1045519]]]}, u'country_code': u'CL', u'attributes': {}, u'id': u'008be613029d4ca5', u'name': u'Vi\xf1a del Mar'
coordinates field :
{u'type': u'Point', u'coordinates': [-71.546977, -33.025606]}
geo field :
{u'type': u'Point', u'coordinates': [-33.025606, -71.546977]}
location field of user field:
location :  大日本帝国
'''
