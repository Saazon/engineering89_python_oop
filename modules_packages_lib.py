# Python's extensive documentation on python.org
# We have used functions that we ecreated as well as the built in ones
#
# import is the keyword that is used to import any module available in python.org
# Let's see that in action
# Mathematics
import math
import random

num1 = 23.44 # Float

# In a real life situation you have to round the figure depending on the value
# If the value is less than .50 round it down to 23, if .51 then round it up

print(math.ceil(num1))
print(math.floor(num1))

# Random class/methods
print(random.random())
# Generates a random number between 0 and .99

# How can we interact with our machine using python?
import os # This usually sits at the top of the file, but for readabilities sake it's here for now, os used to get information about your OS
import datetime, sys # sys used to get system specific information

word_dir = os.getcwd() # provides the current location/path
print(word_dir)

# Linux/macOS
print(os.getuid)
print(os.cpu_count())
print(os.uname())

# The problem with this is that you are going to have software that is run by people on ALL OS's, so building OS specific tools can be a bad idea

print(datetime.datetime.today()) # Today's date
print(sys.path)
# type() len()

import requests # requests is a package to interact with a live API
# we can make an API call to any web address using python requests packages
# pip is a package manager in python to install any packages
# pip install requests
import requests

requests_api = requests.get("https://spartaglobal.com")

print(requests_api.status_code) # Prints the status code; 200 success, 404 not found etc.
print(requests_api.headers) # Prints headers
print(requests_api.content) # Prints out the HTML source

print(type(requests_api.status_code)) # Prints the type.
print(type(requests_api.headers))
print(type(requests_api.content))
