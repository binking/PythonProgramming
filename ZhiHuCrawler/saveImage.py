# You should remeber how to use os module
from urllib import request, error
import bs4 as beautifulsoup
import re, os

def save_img(path, url, img_order):
    try:
        picture = request.urlopen(url).read()
    except error.URLError as e:
        print(e)
        return False

    if not os.path.exists(path):  # Createing folder path
        os.makedirs(path)
    f = open('%s%03d.jpg' % (path, img_order), "wb")
    f.write(picture) # Data flow redirect
    f.flush()
    f.close()

def save_text(path, name, text):
    if not os.path.exists(path):  # Createing folder path
        os.makedirs(path)
    f = open('%s%s.txt' % (path, name), "w")
    f.write(text)
    f.flush()
    f.close()