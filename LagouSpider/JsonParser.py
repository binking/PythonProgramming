import json, re
from pandas import DataFrame, Series
from bs4 import BeautifulSoup
import pandas as pd
from urllib import request

def JsonParser(lagou_api):
	#读取json数据，开始解析
    try:
    	jsondata=json.loads(str(lagou_api,encoding='utf-8',errors='ignore'))["content"]['positionResult']['result']
    	for t in list(range(len(jsondata))):
    	#把company描述的列表合并为一个字符串
    		jsondata[t]['companyLabelList2']='-'.join(jsondata[t]['companyLabelList'])
    		jsondata[t].pop('companyLabelList')
    		#print(jsondata[t])
    		#print()
    		#将每一行数据做成Series，之后再合并
    		if t == 0:
	    		rdata=DataFrame(Series(data=jsondata[t])).T
    		else:
    			rdata=pd.concat([rdata,DataFrame(Series(data=jsondata[t])).T])
    	#重新给rdata编码
    	rdata.index=range(1,len(rdata)+1)
    	# rdata['keyword']=keyword
    	rdata['salarymin']=0
    	rdata['salarymax']=0
    	rdata['url']=''
    	rdata['jd']=''#职位描述
    	rdata['handle_perc']=''#简历及时处理率，在七天内处理完简历占所有简历的比例
    	rdata['handle_day']=''#完成简历处理平均天数
    	print("88888888888888888888888888888888**")
    	for klen in list(range(len(rdata['salary']))):
    		rdata.ix[klen+1,'salarymin'] = re.search('^(\d*?)k',rdata['salary'].iloc[klen]).group(1)
    		#如果工资的最大值没有写，如（8k以上），则列为空值
    		if re.search('-(\d*?)k$',rdata['salary'].iloc[klen]) != None:
    			rdata.ix[klen+1,'salarymax'] = re.search('-(\d*?)k$',rdata['salary'].iloc[klen]).group(1)
    		else:
    			rdata.ix[klen+1,'salarymax'] = ''
    			#增加url一列，便于后续抓取jd内容
    		rdata.ix[klen+1,'url'] =  'http://www.lagou.com/jobs/%s.html'% rdata.ix[klen+1,'positionId']
    		#对url进行二次抓取，把jd抓进来
    		# print("*******************************88")
    		with request.urlopen(rdata.ix[klen+1,'url']) as f:
    			data_url=f.read()
    			soup_url=BeautifulSoup(data_url,'html5lib')
    			strings_url=soup_url.find('dd',class_='job_bt').strings
    			rdata.ix[klen+1,'jd']=''.join(strings_url).encode('gbk','ignore').decode('gbk','ignore').replace(' ','')
    			temp=soup_url.find_all('span',class_='data')
    			if re.search('>(\w*%)<',str(temp[0])) == None:
    				rdata.ix[klen+1,'handle_perc']=''
    			else:
    				rdata.ix[klen+1,'handle_perc']=re.search('>(\w*%)<',str(temp[0])).group(1)
    			rdata.ix[klen+1,'handle_day']=re.search('>(\w*)<',str(temp[1])).group(1).replace('天','')

    except Exception as e:
    	print(e)
    	#构造totaldata，是所有页面的集合，rdata是这一个页面的集合
    if i == 0:
    	totaldata=rdata
    else:
    	totaldata=pd.concat([totaldata,rdata])

    totaldata.index=range(1,len(totaldata)+1)
    print('正在抓取搜索页面第%d页,时间是%s，还剩下%d页'%(i+1,datetime.datetime.now(),urlcount-i-1))

    #开始写入数据库
    print(totaldata)
    totaldata.to_excel('lagou.xls',sheet_name='sheet1')