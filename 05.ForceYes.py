# Project 5: Jason Huang

#if else statement won't work, the loops isn't enough
#implement your own validation rules

while True:
    response = raw_input("Do you like turtles? ")
    if response != "yes":
        print ("I don't like the answer; do you like turtles?")
        continue
    else:
        print "Congratulations!"
        break