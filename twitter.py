#!/usr/bin/env python2

import sys
from TwitterSearch import *

# Function to exit program with printing error


def pexit(str):
    print("Error: " + str)
    exit()

# Main function


def main():

    keyword1 = ""
    keyword2 = ""

    # checking passed arguments
    if(len(sys.argv) == 1):
        keyword1 = raw_input("Enter first keyword: ")
        keyword2 = raw_input("Enter second keyword: ")
    elif(len(sys.argv) == 3):
        keyword1 = sys.argv[1]
        keyword2 = sys.argv[2]
    else:
        pexit("Invalid arguments!")

    print("First arg: {}\nSecond arg: {}".format(keyword1, keyword2))

    try:
        tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
        # let's define all words we would like to have a look for
        tso.set_keywords(['Soccer'])
        tso.set_language('en')  # we want to see German tweets only
        # and don't give us all those entity information
        tso.set_include_entities(False)

        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key='oGiyPgV3omQdW3WGbH1G6LCJh',
            consumer_secret='17lUrRkBZt5ao07Y4gLU3WpMEbXeE351mKyo2KuIDJItYcxTqa',
            access_token='809106133113798656-25cBjTKjcdSupDcMdWuGx42S46WLTVD',
            access_token_secret='v59tfw8T2pKFxop6qdCBuLEEyfCf326Z58aGlEtxb9jEy'
        )

        # this is where the fun actually starts :)
        for tweet in ts.search_tweets_iterable(tso):
            print('@%s tweeted: %s' %
                (tweet['user']['screen_name'], tweet['text']))

    except TwitterSearchException as e:  # take care of all those ugly errors if there are some
        print(e)


if __name__ == "__main__":
    main()
