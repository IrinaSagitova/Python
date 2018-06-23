import requests
from urllib.parse import urlencode

app_id = '1adc1695e4dd46f5ae54ebf6c1ff8016'
auth_url = 'https://oauth.yandex.ru/authorize'

auth_data = {
	'client_id': app_id,
	'response_type': 'token'
}

#print('?'.join((auth_url, urlencode(auth_data))))

#token = 'AQAAAAAWg2DaAATqKHvV2qn0NEFruosLVlLrzss'
#params = {
 # 'oauth_token': token, 
#}
#response = requests.get('https://api-metrika.yandex.ru/management/v1/counters', params)
#counter_id = response.json()['counters'][0]['id']

#params = {
 # 'id': counter_id,
  #'metrics': 'ym:s:visits'
#}

#headers = {
	#'authorization': 'oauth {}'.format(token)
#}

#response = requests.get('https://api-metrika.yandex.ru/management/v1/data', params, headers=headers)
#print(response.text)

class YaBase:
	def __init__(self, token):
		self.token = token

	def get_headers(self):
		return {
			'authorization': 'oauth {}'.format(self.token)
		}


class YaMetricaUser(YaBase):
	def get_counters(self):
		headers = self.get_headers()
		response = requests.get('https://api-metrika.yandex.ru/management/v1/counters', headers=headers)
		return [c['id'] for c in response.json()['counters']]

class Counter(YaBase):
	def __init__(self, counter_id, token):
		self.counter_id = counter_id
		super().__init__(token)

	def get_visits(self):
		headers = self.get_headers()
		params = {
			'id': self.counter_id,
			'metrics': 'ym:s:visits'
		}	
		response = requests.get('https://api-metrika.yandex.ru/management/v1/data', params, headers=headers)
		try:
			return response.json()['data'][0]['metrics'][0]
		except IndexError as e:
			return e	 
	
	def get_views(self):
		headers = self.get_headers()
		params = {
			'id': self.counter_id,
			'metrics': 'ym:s:pageviews'
		}
		response = requests.get('https://api-metrika.yandex.ru/management/v1/data', params, headers=headers)
		try:
			return response.json()['data'][0]['metrics'][0]
		except IndexError as e:
			return e

	def get_users(self):
		headers = self.get_headers()
		params = {
			'id': self.counter_id,
			'metrics': 'ym:s:users'
		}
		response = requests.get('https://api-metrika.yandex.ru/management/v1/data', params, headers=headers)
		try:
			return response.json()['data'][0]['metrics'][0]
		except IndexError as e:
			return e



first_user = YaMetricaUser('AQAAAAAWg2DaAATqKHvV2qn0NEFruosLVlLrzss')
counters = first_user.get_counters()
print(counters)	
for counter_id in counters:
	counter = Counter(counter_id, first_user.token)
	visits = counter.get_visits()
	print(visits)
for counter_id in counters:
	counter = Counter(counter_id, first_user.token)
	views = counter.get_views()
	print(views)
for counter_id in counters:
	counter = Counter(counter_id, first_user.token)
	users = counter.get_users()
	print(users)
