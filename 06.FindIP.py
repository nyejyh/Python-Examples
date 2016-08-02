# Project 6: Jason Huang
import socket
response = raw_input("Please enter the domain name you want to find IP for: ")
print socket.gethostbyname(response)
address = socket.gethostbyname(response)
print ('The IP address of {0} is {1}.'.format(response, address))