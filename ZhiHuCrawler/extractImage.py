#!/usr/bin/env python3
# Idea : crawl all answer of one question, and store them in our MySQL db
# table ques_name
# Answer_id   who  content(text)   hyperlink   picture     num_of_upvote   num_of_scanning     num_of_care     num_of_related
# Answer_id:<a>---<name>,e.g:<a class="zg-anchor-hidden" name="answer-28301743"></a>\n\n
# who: <link rel="canonical" href="https://www.zhihu.com/people/user_name" />; Chinese name were transormed into PinYin
# Problems:
# 1. How to address the Chinese messy code of content -- u"姹熸櫤褰?.encode(); store();"hex_code".decode()
# 2. How to store picture  -- Change pitures into data flow
# 3. Collect some important numbers

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
    f = open('%s/%03d.jpg' % (path, img_order), "wb")
    f.write(picture) # Data flow redirect
    f.flush()
    f.close()

def Main():
    zhimg_url = "http://www.duanzhihu.com/answer/28308001" # One special page of Zhihu full of fb battle images
    html = request.urlopen(zhimg_url).read() # In python3, request module hid in urllib
    soup = beautifulsoup.BeautifulSoup(html, "html.parser") # Instantialize an bs4 instance
    tag_a = soup.find_all("img") # Get all <img> tags
    img_urls =[]
    white_dot = r'whitedot.jpg'
    for link in tag_a:
        img_link1 = link.get('data-original', None) # Some data-original is same as src, for example Wang's Ignorance
        img_urls.append(img_link1)
        img_link2 = link.get('src', None) # get all links of the page
        if not re.search(white_dot, img_link2):
            img_urls.append(img_link2)
    order = 0
    for img in img_urls:
        order += 1
        print(img)
        save_img('./ZhiHuImg/', img, order)


if __name__ == "__main__":
    Main()
