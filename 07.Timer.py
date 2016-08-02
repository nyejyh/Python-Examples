# Project 7: Jason Huang

#populate a list
#numbra = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#get user's response to check with list
import time
import sys

while True:
    response = int(raw_input("Please enter a number between 1 and 10.  Outside value will reset: "))
    for i in range(1, 11):
        if (response == i):
            print ('The number you entered is {0}.'.format(response))
            time.sleep(1)
            while response != 0:
                response -= 1
                time.sleep(1)
                print ('The number is now counting down, and is {0}.'.format(response))
        if (response == 0):
            print "This program has finished counting down, and will now exit."
            sys.exit()
        else:
            #print "The number you entered lies outside of the range between 1 and 10."
            continue
            