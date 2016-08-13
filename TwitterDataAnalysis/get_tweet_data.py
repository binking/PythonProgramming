# Jiangzhibin
import oauth2 as oauth
import urllib, http
import urllib.request
#import json
# See assignment1.html instructions or README for how to get these credentials

api_key = "B1uB90Z0CpcaFmzkeJ9NHqOYh"
api_secret = "2eCI6Y3pPwt3ObPBYpru08VvWgJndLqQx7Y96i3EYt5O551Lid"
access_token_key = "4567647824-zUOChj4BWkDNia3Rd0fIgrHbLGnM0rai1C2ITzy"
access_token_secret = "HQhI0oVRymS5dr1waI3Fnr3GK7hsrsFU2li12q7ORmaUb"

_debug = 0
oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)
signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()
http_method = "GET"
http_handler  = urllib.request.HTTPHandler(debuglevel=_debug)
https_handler = urllib.request.HTTPSHandler(debuglevel=_debug)

fr = open('tweets_1.json', 'w')
'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)
    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)
    headers = req.to_header()
    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()
    opener = urllib.request.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)
    response = opener.open(url, encoded_post_data)
    return response

def fetchsamples(num):
  url = "https://stream.twitter.com/%d/statuses/sample.json" % num
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    #fr.write(json.dumps(line)) # To Address : http.client.IncompleteRead: IncompleteRead(0 bytes read, 1 more expected)
    fr.write(line.strip().decode("utf-8"))
'''
def fetchsamples():
    parameters = []
    for i in range(1,11):
        url = "https://stream.twitter.com/%d/statuses/sample.json" % i
        response = twitterreq(url, "GET", parameters)
        print(i)
        try:
            for line in response:
                fr.write(json.dumps(line) + '\n')
        except Exception as e:
            pass
'''
if __name__ == '__main__':
    num = 1
    while True:
        try:
            fetchsamples(num)
        except Exception as e:
            print(e)
            num += 1
            print(num)
            continue
