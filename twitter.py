import sys


#Function to exit program with printing error
def pexit(str):
    print("Error: " + str)
    exit()

#Main function
def main():
    
    #checking passed arguments
    if(len(sys.argv) != 3):
        pexit("Insufficient number of arguments!")

    keyword1 = sys.argv[1]
    keyword2 = sys.argv[2]

    print("First arg: {}\nSecond arg: {}".format(keyword1, keyword2))


if __name__ == "__main__":
    main()