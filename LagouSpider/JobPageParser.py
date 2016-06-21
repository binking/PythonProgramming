import requests, re
from bs4 import BeautifulSoup

def extractJobDescr(jobid):
    page = 'http://www.lagou.com/jobs/{jid}.html'
    with request.urlopen(page.format(jid=jobid)) as uf:
        data_url = uf.read()
        dd_tag = BeautifulSoup(data_url,'html5lib')
        strings_url = dd_tag.find('dd',class_='job_bt').strings
        # rdata.ix[klen+1,'jd']=''.join(strings_url).encode('gbk','ignore').decode('gbk','ignore').replace(' ','')
        jd = =''.join(strings_url).encode('gbk','ignore').decode('gbk','ignore').replace(' ','')
        span_tag = soup_url.find_all('span',class_='data')
        if re.search('>(\w*%)<',str(span_tag[0])) == None:
             # rdata.ix[klen+1,'handle_perc']=''
             handle_perc = ''
        else:
             # rdata.ix[klen+1,'handle_perc']=re.search('>(\w*%)<',str(temp[0])).group(1)
             handle_perc = re.search('>(\w*%)<',str(span_tag[0])).group(1)
        # rdata.ix[klen+1,'handle_day']=re.search('>(\w*)<',str(temp[1])).group(1).replace('天','')
        handle_day = re.search('>(\w*)<',str(span_tag[1])).group(1).replace('天','')
        return jd, handle_perc, handle_day
