# pip install pyshorteners(library used in this code)
# pip install pyperclip

import pyshorteners

url = input("Paste the url to shorten:")


def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))


print("The short url is:\n")
shortenurl(url)  # Displays the shorted url
