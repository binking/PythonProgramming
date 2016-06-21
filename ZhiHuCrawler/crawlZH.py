# the directories tree like this:
# question_id :
# ---question_info.txt
# ---answer_if:
# -------answer_info.txt
# -------answer_content.txt
# -------picture:
# ----------000.jpg
# ----------001.jpg
# and so on
# Finally, let's store all documents into Mongodb

from question import Question
from answer import Answer
from mongodb import MongoDB
from saveImage import save_img, save_text
from urllib import request, error

q = Question("https://www.zhihu.com/question/39547745")
q.setting()
answer_list = q.get_answer_id_list()
#q_info = 'Title : '+q.title+'\nQuestion url : '+q.qurl+'\nQuestion id : '+\
#        str(q.qid)+'\nAsker : '+q.asker+'\nNumber of Follows : '+str(q.num_of_follows)+\
#        '\nNumber of Comments : '+ str(q.num_of_comments)+'\nNumber of Answers : '+str(q.num_of_answers)
#save_text('./%s/' % str(q.qid), str(q.qid)+'_info', q_info)
mongo = MongoDB(str(q.qid), False) # in inintialization, it will connect Mongodb server
'''
mongo.insertData('Questions', {
        'title': q.title,
        'question_url': q.qurl,
        'question_id': q.qid,
        'asker': q.asker,
        'num_of_follows': q.num_of_follows,
        'num_of_comments': q.num_of_comments,
        'num_of_answers': q.num_of_answers,
        'answers_list': answer_list,
        })
# Insert all data
for answer_id in answer_list:
    a = Answer(answer_id)
    a.setting()
    print("Store info of %s into Mongodb Server" % ('http://www.duanzhihu.com/answer/'+answer_id))
    i = 0; image_flow = []
    for img_url in a.img_list:
        i += 1
        image_flow.append(request.urlopen(img_url).read())
    result = mongo.insertData('Answers', {
                'answer_id': answer_id,
                'time': a.time,
                'anthor': a.author,
                'upvotes': a.upvotes,
                'content': a.content,
                'pirture_bit': image_flow,
                })
    print(result.inserted_id)
        #print('\tImage url: ', img_url)
        #save_img('./%s/%s/picture/' % (q.qid, answer_id), img_url, i)
    #basic_info ='Answer id :'+a.aid+'\nAnthor : '+a.author+'\nTime : '+a.time+'\nUpvotes : '+str(a.upvotes)
    #save_text('./%s/%s/' % (str(q.qid), answer_id), answer_id+'_info', basic_info)
    #save_text('./%s/%s/' % (str(q.qid), answer_id), answer_id+'_content', a.content)
'''
# Query by some specific conditions
ques_res = mongo.queryData('Questions')
for res in ques_res:
    print(res)

ans_res = mongo.queryData('Answers')
for res in ans_res:
    print(res)

mongo.stopMongoDB()


