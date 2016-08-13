from urllib import request, error
from bs4 import BeautifulSoup
import re
# To be honest, find to position of specific numbers or urls is difficult
# if you don't know anything about HTML/CSS/JavaScript
class Question():
    qurl = ''  # record url of the question
    qhtml = '' # record page code of the question
    asker = title = u'' # record who asks the question and its title
    qid = 0
    num_of_follows = num_of_answers = num_of_comments = 0
    # record number of Follows, Answers, Comments
    def __init__(self, url):
        self.qurl = url
        self.qid = eval(url.split("/")[-1])
        self.qhtml = request.urlopen(url).read() # read(), return data flow --- b''
        self.num_of_follows = self.num_of_answers = self.num_of_comments = 0
        self.asker = self.title = u''

    def set_num_of_follows(self):
        soup = BeautifulSoup(self.qhtml, "html.parser") # Without "html.parser", it warned
        div_tags = soup.find_all("div")
        for div_tag in div_tags:
            #print(div_tag.get("class", None))
            if div_tag.get('class', None) != None and\
             'zm-side-section-inner' in div_tag.get('class', None) and\
             "zg-gray-normal" in div_tag.get('class', None) :
             # filter those div_tag without class attr
             # find num of follows by using class attrs of 'zm-side-section-inner' and 'zm-gray-normal'
                self.num_of_follows = eval(div_tag.text.split('\n')[-4])
                # There are serval lines in this div's text, but we just need one line---the num
                return 0
        print("Can not find the number of follows")
        return -1

    def set_num_of_answers(self):
        soup = BeautifulSoup(self.qhtml, "html.parser")
        h3_tags = soup.find_all("h3") # the num of answers hidden in <H3>
        for tag in h3_tags: # But there are many <H3> tags
            if tag.get('id', None) == 'zh-question-answer-num' : # Find the <H3> whose id is 'zh-question-answer-num'
                self.num_of_answers = tag.get('data-num', None) # get it
                return 0
        print("Can not find number of answer")
        return -1

    def set_num_of_comments(self):
        soup = BeautifulSoup(self.qhtml, "html.parser")
        a_tags = soup.find_all("div", {"class":"zm-meta-panel"}) # the num of comments hidden in <DIV> with class attr of 'zm-meta-panel'
        self.num_of_comments = eval(a_tags[0].find_all("a")[0].text.split(' ')[0])

    def set_title(self):
        soup = BeautifulSoup(self.qhtml, "html.parser")
        head_html = soup.find_all("h2") # the title of question hidden in <H2>tag
        self.title = head_html[0].text.strip()

    def get_answer_id_list(self):
        ans_list = []
        soup = BeautifulSoup(self.qhtml, "html.parser")
        div_tags = soup.find_all("div")
        for div_tag in div_tags:
            if div_tag.get("data-aid", None):
                ans_list.append(div_tag.get("data-aid"))
        return ans_list

    def setting(self, attr_list = []):
        '''
        the general of all attributes setting 
        '''
        methods = {'title': self.set_title, 'num_of_answer': self.set_num_of_answers,\
                    'num_of_comments': self.set_num_of_comments, 'num_of_follows': self.set_num_of_follows}
        if attr_list ==[]: # If attr_list is empty, set all of settings
            self.set_title(); self.set_num_of_answers();self.set_num_of_comments();self.set_num_of_follows()
        else:
            for attr in attr_list:
                fun = methods[attr]
                fun()
'''
oneQues = Question('https://www.zhihu.com/question/39547745')
oneQues.setting(['title', 'num_of_follows'])
print('question id : ', oneQues.qid, 'question url : ', oneQues.qurl)
print(oneQues.title, '\tAnswer:', oneQues.num_of_answers, '\tFollows:',\
            oneQues.num_of_follows, '\tComments:', oneQues.num_of_comments)
print(oneQues.get_answer_id_list())

    def set_num_of_follow_by_re(self):
        #To be Continued, I am not resignd to
        reg = r'/question/39547745/followers'
        follows = re.search(reg, self.qhtml.decode())
        print(follows)
        if follows != None:
            self.num_of_follows = follows
            return 0
        else:
            return -1

def test():
    oneQues = Question('https://www.zhihu.com/question/39547745')
    oneQues.set_title(); oneQues.set_num_of_answer();
    oneQues.set_num_of_comments();oneQues.set_num_of_follow()
    print('question id : ', oneQues.qid, 'question url : ', oneQues.qurl)
    print(oneQues.title, '\tAnswer:', oneQues.num_of_answers, '\tFollows:',\
            oneQues.num_of_follows, '\tComments:', oneQues.num_of_comments)
    print(oneQues.get_answer_id_list())

if __name__ == "__main__":
    test()
'''