import argparse
import oauth2 as oauth
import urllib.request as urllib
import json
import sys
import csv

# See Assignment 1 instructions for how to get these credentials
access_token_key = "98634446-VDFrDGT5tQ7IzoCrVePmUwx8NdgJnPJjJMllykYuJ"
access_token_secret = "Z8eVZk7RsXCIcnD3QxQZ4KEyxmHjCI4jUq0pkd4zEWf1F"

consumer_key = "m6RL7LwXv03RYBPh6CPpq9w5D"
consumer_secret = "qPiVQNYQ5dPdICpM4kyBFHWAEwxkoSwDy0PXgawAkHy7mNMdmx"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

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

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response

def fetch_samples():
    url = "https://stream.twitter.com/1.1/statuses/sample.json?language=en"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    #responseString = response.read().decode('utf-8')
    for line in response:

        print (line.strip().decode('utf-8'))

def fetch_by_terms(term):
    url = "https://api.twitter.com/1.1/search/tweets.json"
    parameters = [("q", term),("count",100),("language","en")]

    response = twitterreq(url, "GET", parameters)
    print (response.readline().decode('utf-8'))

def fetch_by_user_names(user_name_file):
    #TODO: Fetch the tweets by the list of usernames and write them to stdout in the CSV format
    sn_file = open(user_name_file)
    url="https://api.twitter.com/1.1/statuses/user_timeline.json"
    writer = csv.writer(sys.stdout)

    for line in sn_file:
        parameters=[("screen_name",line),("count",100)]
        response = twitterreq(url,"GET",parameters)
        tweetJSON=response.readline().decode('utf-8')
        tweets=json.loads(tweetJSON)
        screen_name=line.strip()
        #print (tweet)
        

        
        #     break
        if type(tweets).__name__ == "dict":
            continue
        for tweet in tweets:
            # for key in tweet:
            #     if key=='error':
            #         break
            #     # if key == 'error':

            #     #     break
            #     # else:
            #     #if type(tweet[key]) is dict and tweet[key].get('text',False):
            #     else:
            #      

            #print (tweet['text'].encode('utf‐8'))
            tweet_text = tweet['text']
            tweet_text = tweet_text.replace("\n"," ")
            writer.writerow([screen_name,tweet_text])
                
        # print (tweet['text'].encode('utf‐8'))
        #break
    #writer = csv.writer(sys.stdout)






if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', required=True, help='Enter the command')
    parser.add_argument('-term', help='Enter the search term')
    parser.add_argument('-file', help='Enter the user name file')
    opts = parser.parse_args()
    if opts.c == "fetch_samples":
        fetch_samples()
    elif opts.c == "fetch_by_terms":
        term = opts.term
        print (term)
        fetch_by_terms(term)
    elif opts.c == "fetch_by_user_names":
        user_name_file = opts.file
        fetch_by_user_names(user_name_file)
    else:
        raise Exception("Unrecognized command")
