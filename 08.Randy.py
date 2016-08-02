# Project 8: Jason Huang
import random
import sys

while True:
    response = int(raw_input("Please enter a number between 1 and 100.  Outside value will reset: "))
    for i in range(0, 101):
        if (response == i):
            print ('The number you entered is {0}.'.format(response))
            new1 = random.randint(1, response)
            new2 = random.randint(1, response)
            new3 = random.randint(1, response)
            new4 = random.randint(1, response)
            new5 = random.randint(1, response)
            print ('The first random number between 1 and {0} is {1}.'.format(response, new1))
            print ('The second random number between 1 and {0} is {1}.'.format(response, new2))
            print ('The third random number between 1 and {0} is {1}.'.format(response, new3))
            print ('The fourth random number between 1 and {0} is {1}.'.format(response, new4))
            print ('The fifth random number between 1 and {0} is {1}.'.format(response, new5))
            sys.exit()
        else:
            continue