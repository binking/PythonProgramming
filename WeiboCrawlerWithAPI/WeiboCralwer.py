from weibo import Client
import time

class WeiboCralwer(object):
	"""docstrinWeiboCralwerg for """
	def __init__(self, myid, **client_arg):
		# client_arg should be {API_KEY, API_SECRET, REDIRECT_URL, AUTH_URL, USER_NAME, USER_PWD}
		self.myid = myid
		self.client_arg = client_arg
		self.remaining_user_access = 0
		self.remaining_ip_access = 0
		self.wait_time = 0
		self.weibo_i = None

	def loginWeibo(self):
		try:
			self.weibo_i = Client(self.client_arg['API_KEY'], self.client_arg['API_SECRET'], \
					self.client_arg['REDIRECT_URL'], self.client_arg['token'])
		except Exception as e:
			print("Login failed")

	def checkLimit(self):
		limit_result = self.weibo_i.get('account/rate_limit_status', uid=self.myid)
		self.wait_time = limit_result['reset_time_in_seconds'] + 300 # if meet limit, sleep 300+ seconds
		self.remaining_ip_access = limit_result['remaining_ip_hits']
		self.remaining_user_access = limit_result['remaining_user_hits']
		return self.remaining_ip_access, self.remaining_user_access

	def get_friends_ids(self, uid):
		next_cursor = 0
		friends_ids_list = []
		while(True):
			result = self.weibo_i.get('friendships/friends/ids', uid=uid, cursor=next_cursor)
			ids_list = result['ids']
			next_cursor += len(ids_list)
			# print(ids_list)
			if len(ids_list) == 0:
				break
			friends_ids_list.extend(ids_list)
		return friends_ids_list

	def get_friends_info(self, uid):
		next_cursor = 0
		friend_info_list = []
		while(True):
			result = self.weibo_i.get('friendships/friends', uid=uid, cursor=next_cursor)
			user_list = result['users']
			next_cursor += len(user_list)
			if len(user_list) == 0:
				break
			friend_info_list.extend(user_list)
		return friend_info_list

	def get_blogs_by_ids(self, uid, group_id):
		# This access need more advanced permission
		results = self.weibo_i.get('statuses/show_batch', ids=group_id)
		for res in results:
			print("Weibo id: %d --> Text: %s" % (res.get("statuses", {}).get("id")))

	def delay():
		print("Stopping, begin after %s seconds" % self.wait_time)
		time.sleep(self.wait_time)