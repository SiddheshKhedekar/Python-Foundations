"""
The program takes in a text file reads it's contents and then verifies it against an online profanity checker api to give profanity alerts if any.
"""

# import urllib for web api query request functions
import urllib

# function to read the text
def read_text():
	# Specify where the text file is either full address or keep in same folder
	quotes = open("movieQuotes.txt")
	# read contents of the file
	contents_of_file = quotes.read()
	# file closed
	quotes.close()
	# call profanity checker function
	check_profanity(contents_of_file)

# function to check profanity
def check_profanity(text_to_check):
	# Profanity checker website
	base_url = "http://www.purgomalum.com/service/containsprofanity"
	query_str = "?text=" + text_to_check
	# query to api sent
	connection = urllib.urlopen(base_url + query_str)
	# response read
	output = connection.read()
	# connection closed
	connection.close()
	# display profanity response as per output
	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("Cound not scan the document properly.")

# call function to read a file to check its profanity
read_text()
