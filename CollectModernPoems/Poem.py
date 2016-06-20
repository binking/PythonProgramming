#/usr/bin/env python3
from bs4 import BeautifulSoup
import requests, jieba, re, time
from requests.exceptions import ConnectionError
reExp_url = r'http://.+/XianDai(.+)\.html'

class Poem():
    def __init__(self, url):
        self.poem_url = url
        self.id = re.search(reExp_url, url).groups()[0]
        try :
            response = requests.get(url)
        except ConnectionError as e:
            print('Error emerged : ')
            print("Hey, Binking, connection error came again, maybe you need to wait for 15s ")
            time.sleep(15) # Deal with requests.exceptions.ConnectionError: HTTPConnectionPool(host='www.chinapoesy.com', port=80): 
            #Max retries exceeded with url: /XianDaiEB8D7A41-6848-4B3C-8579-6AA60B00CBD1.html (Caused by NewConnectionError
            #('<requests.packages.urllib3.connection.HTTPConnection object at 0x000000000687D2B0>: 
            #Failed to establish a new connection: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，
            #连接尝试失败。',))
            response = requests.get(url) # After it wake up, try access again
        finally:
            self.pageSoup = BeautifulSoup(response.text, 'html.parser')
        self.text = self.setText()
        self.title, self.author = self.setTitleAndAuthor()
        self.wordCount = self.parseText()

    def setTitleAndAuthor(self):
        '''<title>
    title
——vice title_Author一诗歌_近现代诗歌_诗词在线--中国最具影响力的开放式原创诗词网站
</title>
        '''
        head = self.pageSoup.find('title')
        head = head.text.encode('gbk', 'ignore').decode('gbk').strip().split('_')
        return ''.join(head[0].split()), head[1][:-2]  # Because of the new line letter embed in title

    def setText(self):
    	script_tags = self.pageSoup.findAll('script', {'type': 'text/javascript'})
    	#print(script_tags[9].text.strip())
    	poem_text = script_tags[9].find_next('p')
    	if len(poem_text.text) < 20:
    		poem_text = script_tags[9].find_next('div')
    	return poem_text.text.encode('gbk', 'ignore').decode('gbk').split()[2:]

    def parseText(self):
        allWords = []; wc = {}
        for sentence in self.text:  # sentence is a string
            #allWords.extend(sentence)
            seg_list = list(jieba.cut(sentence, cut_all=False))  # Accurate mode
            allWords.extend(seg_list)  # the obj that cut returns only can be used in one time
        wordSet = set(allWords)  # allWords has same words while wordSet not
        #print('herererddvdfvfv')
        for word in wordSet:
            wc[word] = allWords.count(word)
        return wc
'''
    def setText(self):
        # Because the p tag of body has not attrs, so find the p tag of name first
        # and then find next p tag that is our target
        #print(self.pageSoup.text.encode('gbk', 'ignore').decode('gbk'))
        #ghost_p_tag = self.pageSoup.find('p', attrs = {'style': 'text-align: center;'}) # I called it ghost, it's diffcult to find
        #print(ghost_p_tag.text.encode('gbk', 'ignore').decode('gbk'))
        try:
        	ghost_p_tag = self.pageSoup.find('p', attrs = {'style': 'text-align: center;'}) 
        	ghost_text = ghost_p_tag.text
        except AttributeError as e:
        	try:
        		ghost_p_tag = self.pageSoup.find('p', attrs = {'Style': 'text-align: center;'})
        		ghost_text = ghost_p_tag.text
        	except AttributeError as e:
        		try:
        			ghost_p_tag = self.pageSoup.find('div', attrs = {'Style': 'text-align: center;'})
        			ghost_text = ghost_p_tag.text
        		except AttributeError as e:
        			ghost_text = ''
        finally:
        	return ghost_text
'''
# .find('p', attrs = {'style': 'text-align: center;'})
# .find('p', attrs = {'style': 'text-align: center;'})
