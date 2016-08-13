#/usr/bin/env python3
# The directory should  like this :
# Database : ModernPoems
# ---- Index Page Order (Folder/collection):
# ---- ---- Poem_ID list
import re
from bs4 import BeautifulSoup
import requests, os, csv, time
from Poem import Poem

def parseIndexPage(url):
    # Find the table of list of poems
    index_soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    poems_urls = []
    table_of_poems = index_soup.find('table', attrs={'class':'List'})  # Now I found the aimed table
    for tr in table_of_poems.find_all('tr'): # Now I should extract all urls pointed to peoms
        for td in tr.findAll('td'):
        	poems_urls.append('http://www.chinapoesy.com/' + td.find('a').get('href'))
    return poems_urls

def main():
    dataset = []; i = 1
    with open('poetry_dataset.csv', 'wt') as pcsv:
        p_writer = csv.writer(pcsv, delimiter='\t')
        p_writer.writerow(['Order', 'Id', 'Author', 'Url', 'Title', 'Text', 'Word_Count'])
        for order in range(1, 84):
            print(order)
            index_page = 'http://www.chinapoesy.com/XianDaiList_%d.html' % order # 83 index pages at most
            peom_link_list = parseIndexPage(index_page)
            for poem_link in peom_link_list:
                poem = Poem(poem_link)
                p_writer.writerow([i, poem.id, poem.author, poem.poem_url, poem.title, poem.text, poem.wordCount])
                i += 1
			    #print(poem.id)
    		    #print(poem.author)
    		    #print(poem.poem_url)
                print(poem.title)
                #print(poem.text.encode('gbk', 'ignore').decode('gbk').split())
        print(i)
if __name__=='__main__':
    start_time = time.time()
    main()
    print('It takes a long time to finish : ', time.time() - start_time)