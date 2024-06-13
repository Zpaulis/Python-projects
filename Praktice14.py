# let's start with needed standard libraries
# Python version
import sys
print(f"Python version: {sys.version}")
import time # for pausing our web requests so we do not spam the server
from datetime import datetime # for timestamps
# now external libraries
# for web requests
import requests # most crucial library for web scraping
print(f"requests version: {requests.__version__}")

# we will want BeautifulSoup to parse the HTML
from bs4 import BeautifulSoup
# if you do not have BeautifulSoup, you can install it with pip
# !pip install beautifulsoup4 from Notebook
# or
# !pip3 install beautifulsoup4 from terminal for Mac or Linux
# or
# pip install beautifulsoup4 from terminal for Windows
# homepage of BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/

# finally we need Pandas to store the data
import pandas as pd
print(f"Pandas version: {pd.__version__}")

# we know the url what we want to scrape
url = "https://www.ss.com/lv/transport/spare-parts/trunks-wheels/r16/filter/"
print(f"We will scrape the following URL: {url}")

# now we will make a get request to the server at the given URL
response = requests.get(url) # just like our JSON example from last lesson
# there are also post requests and a few others, but get is the most common
# let's check the response and raise error if not 200
if response.status_code != 200:
    raise Exception("Failed to load page")
else:
    print(f"Page loaded successfully from {url}")
# response is not json it is text but marked as HTML
# we could see simply text
# first 1000 characters
print(response.text[:1000])