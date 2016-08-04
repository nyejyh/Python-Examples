#Converter to CBM and price, because I am tired of repetitive calculations.
#Written by Jason Huang 

#Grab user inputted numbers in inches, and number of containers
length = int(raw_input("Please enter the length in inches."))
width = int(raw_input("Please enter the width in inches."))
height = int(raw_input("Please enter the height in inches."))
CTN = int(raw_input("Please enter number of containers."))

#Convert all the inches to meters
nLength = length * 0.0254
nWidth = width * 0.0254
nHeight = height * 0.0254

#Calculate CBM and the pricing with rate.
CBM = nLength * nWidth * nHeight * CTN
price = CBM * 2.50

print ('The calculation is {0}CBM and ${1}.'.format(round(CBM, 4), round(price, 2)))