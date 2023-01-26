#import the pyshorteners module
import pyshorteners

#get the link from the user
link = input("Enter the link : ")

#create a Shortener object
shortener = pyshorteners.Shortener()

#use the tinyurl shortener to shorten the link
x = shortener.tinyurl.short(link)

#print the shortened link
print(x)
