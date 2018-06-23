from urllib.parse import urlencode
import requests
import json

app_id = 6413884
auth_url = 'https://oauth.vk.com/authorize'

auth_data = {
  'client_id': app_id,
  'display': 'mobile',
  'scope': 'friends',
  'response_type':'token',
  'v': '5.73'
}

#print('?'.join((auth_url, urlencode(auth_data))))

token = '65be2913960117348b027fc9bfd7b2aedf3df76a2f8050ffae35281ebba728ca55f12e65beaa636ef285a'
user1_id = input('Введите id первого пользователя: ')
user2_id = input('Введите id второго пользователя: ')

def our_friends(user1_id, user2_id, token):
    params = {
      'access_token': token,
      'v': '5.73',
      'source_uid': user1_id,
      'target_uid': user2_id
    }
    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    friends = json.loads(response.text)
    vk = 'https://vk.com/id'
    for friend in friends['response']:
    	print('id = {}'.format(friend))
      print(vk + str(friend))


our_friends(user1_id, user2_id, token)

        
