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


if __name__ == "__main__":
    main()
