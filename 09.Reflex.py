# Project 9: Jason Huang
# Have not figured out how to replace enter with spacebar command

import random
import time
import timeit

print "Welcome to the League of Reflex!"
print "Try to hit ENTER at the same time the word BANG! appears."


raw_input("Hit ENTER to continue.") #Nothing happens here, still have to press enter to continue

tock = random.randint(0, 10) # Pick a time between 0 and 10 seconds before next command
print ('{0} seconds is the selected time to BANG!.'.format(tock))

start = time.time() # Begin the timer
print ('{0} seconds is the starting time.'.format(start))

time.sleep(tock) # Run the timer to release the BANG
raw_input("BANG!")

end = time.time() # End the timer
print ('{0} seconds is the ending time.'.format(end))

math = end - start - tock # Calculate the difference between display of BANG and enter
print ('The time difference in seconds between you hitting ENTER and BANG! is {0} seconds.'.format(math))