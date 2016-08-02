# Project 2: Jason Huang
#1. store input in variable
#2. scan input for numbers or special characters
#2. scan input for numbers or special character or blank (like you said)
#3. trigger a status change based on boolean output from step 2
#4. depending on status, you have screen output like "this is empty or incorrect or you have numbers, choose new name"
response = raw_input("Please enter your first and last name: ")
print response
print len(response)
# Lists
numeras = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];
# Empty strings are falsy, and mean they are considered false in Boolean context.
if not response:
    print "You cannot leave this blank, please input response again."
# Scan inputs for conditions
for i in response:
    for y in numeras:
        if i == y:
            print "Your name has a number in it, please enter your real name."