from WeiboCralwer import WeiboCralwer

def main():
	deep_1_relation = []
	deep_2_relation = []
	token = {	'access_token': '2.00y3_T4GTW7lKB6a61b61a7f0ev_cO',
				'uid': '5843638692',
				'remind_in': '157679999',
				'expires_at': 1611765566,
			}
	my_id = int(token['uid'])
	cralwer = WeiboCralwer(my_id,
		API_KEY = '1075199565', 
		API_SECRET = 'ec0c5ba34cb2915b176e4d7d4bc8b423', 
		REDIRECT_URL = 'https://api.weibo.com/oauth2/default.html',
		token = token)
	cralwer.loginWeibo()
	deep_1_relation = cralwer.get_friends_ids(my_id)
	print(deep_1_relation)
	#for user_id in deep_1_relation:
#		print("Cralwing user %d " % user_id)
#		deep_2_relation.append(cralwer.get_friends_info(user_id))
#	print(deep_2_relation)
	idstring = str(deep_1_relation[:30])[1:-1].replace(" ", "")
	print(idstring)
	cralwer.get_blogs_by_ids(my_id, idstring)

if __name__ == '__main__':
	main()