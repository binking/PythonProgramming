from urllib import request
from bs4 import BeautifulSoup
import re

time_rexp = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}' # definte the time format in re

class Answer():
    def __init__(self, aid):
        self.aid = aid # Assign the only answer by id, and get its url by id
        self.img_list = [] # record a list of all funny picture urls
        self.content = self.author = self.time = '' # some basic info: author/time/content
        self.upvotes = 0 # record how many people upvote it 

    def extract_content(self):
        '''
        Beacuse the whole page code consists of many similiar parts with same class attrs,
        the div tag we want should be second, cuz the first is of the question
        this method is to find all code of the answer part
        '''
        ahtml = request.urlopen('http://www.duanzhihu.com/answer/' + self.aid) # get the url
        soup = BeautifulSoup(ahtml, "html.parser")
        ans_div = soup.find_all("div", {"class" : "panel panel-info"})[1]
        return ans_div

    def set_time(self):
        ans_div = self.extract_content()
        m = re.search(time_rexp, ans_div.text) # using re to get time
        if m:
            self.time = m.group()

    def set_content(self):
        ans_div = self.extract_content()
        m = re.search(time_rexp, ans_div.text) # using time to split text, the final part is content
        self.content = ans_div.text.split(m.group())[-1].encode('gbk', 'ignore').decode('gbk')
        #### Deal with UnicodeEncodeError: 'gbk' codec can't encode character '\xa0'###
        # This is very important

    def set_upvotes(self):
        ans_div = self.extract_content()
        m = re.search(time_rexp, ans_div.text) # the former part is author and upvotes whose gap is space
        self.upvotes = eval(ans_div.text.split(m.group())[0].split(' ')[-1])

    def set_img_list(self):
        ans_div = self.extract_content()
        img_tags = ans_div.find_all("img")
        white_dot = r'whitedot.jpg' # we don't need whitedot.jpg
        for img_tag in img_tags:
            img_tag1 = img_tag.get('data-original', None) # Some data-original is same as src, for example Wang's Ignorance
            self.img_list.append(img_tag1)
            img_tag2 = img_tag.get('src', None) # get all links of the page
            if not re.search(white_dot, img_tag2):
                self.img_list.append(img_tag2)

    def set_author(self):
        ahtml = request.urlopen('http://www.duanzhihu.com/answer/' + self.aid)
        soup = BeautifulSoup(ahtml, "html.parser")
        title = soup.find("title")
        self.author = title.text.split(' ')[-2]

    def setting(self, attr_list = []):
        methods = {'author': self.set_author, 'img_list': self.set_img_list,\
                    'time': self.set_time, 'upvotes': self.set_upvotes, 'content': self.set_content}
        if attr_list ==[]: # If attr_list is empty, set all of settings
            self.set_author(); self.set_img_list(); self.set_time(); self.set_upvotes(); self.set_content()
        else:
            for attr in attr_list:
                fun = methods[attr]
                fun()
'''
def Test():
    a = Answer('28235030')
    #a.set_author()
    #a.set_img_list()
    #a.set_time()
    #a.set_upvotes()
    #a.set_content()
    a.setting(['author', 'content'])
    print(a.author, a.upvotes, a.time)
    print(a.img_list)
    print(a.content)

if __name__=="__main__":
    Test()
'''