import requests
import json
import time

TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'
USER_ID = '5030613'


class SpyGames:

    def __init__(self, token, user_id):
        self.token = TOKEN
        self.user_id = USER_ID

    def get_friends(self):
        params = {
            'access_token': self.token,
            'v': '5.73',
            'user_id': self.user_id
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        print('*')
        victim_friends_list = response.json()
        return victim_friends_list

    def get_groups(self):
        params = {
            'access_token': self.token,
            'v': '5.73',
            'count': '1000',
            'extended': 0,
            'fields': 'members_count',
            'user_id': self.user_id
        }
        response = requests.get('https://api.vk.com/method/groups.get', params)
        print('*')
        victim_groups_set = set(response.json())
        return victim_groups_set

    def valid_friend(self, victim_friends_list):
        temp_victim_friends_list = ', '.join([str(i) for i in victim_friends_list])
        params = {
            'user_ids': temp_victim_friends_list,
            'v': '5.73'
        }
        response = requests.post('https://api.vk.com/method/users.get', params)
        print('*')
        friends_info = response.json()
        invalid_set_of_friends = set()
        victim_friends_set = set(victim_friends_list)
        for i in friends_info:
            for keys in i:
                if 'deactivated' in keys:
                    invalid_set_of_friends.add(i['id'])
        valid_set_of_friends = victim_friends_set.difference(invalid_set_of_friends)
        valid_list_of_friends = list(valid_set_of_friends)
        return valid_list_of_friends

    def get_friends_groups(self, valid_list_of_friends):
        main_list_friends_groups = []
        i = 1
        for friend in valid_list_of_friends:
            params = {
                'access_token': self.token,
                'user_id': friend,
                'extended': 0,
                'v': '5.73',
                'count': 1000
            }
        response = requests.get('https://api.vk.com/method/groups.get', params)
        print('*')
        time.sleep(0.35)
        try:
            friend_groups_set = set(response.json()['response']['items'])
            main_list_friends_groups.append(friend_groups_set)
            print('Remained friends {}'.format(len(valid_list_of_friends) - i))
            i += 1
        except KeyError:
            print('No access')
        return main_list_friends_groups

    def get_unique_groups(self, victim_groups_set, main_list_friends_groups):
        unique_groups = victim_groups_set.difference(*main_list_friends_groups)
        return unique_groups

    def get_group_description(self, unique_groups):
        list_of_group_description = []
        i = 0
        for user_id in unique_groups:
            params = {
                'group_ids': self.user_id,
                'fields': 'members_count',
                'v': '5.73'
            }
        unused_keys = ['is_closed', 'photo_100', 'photo_200', 'photo_50', 'screen_name', 'type']
        response = requests.get('https://api.vk.com/method/groups.getById', params)
        groups_description = response.json()['response'][i]
        for key in unused_keys:
            del groups_description[key]
        list_of_group_description.append(groups_description)
        i += 1
        return list_of_group_description

    def write_groups_to_json(self, list_of_group_description):
        with open('groups.json', 'w', encoding='UTF-16') as f:
            json.dump(list_of_group_description, f, indent=2, ensure_ascii=False)
            text = json.dumps(list_of_group_description, indent=2, ensure_ascii=False)
            print(text)

    def get_secret_groups(self):
        result_get_groups = self.get_groups()
        result_get_friends = self.get_friends()
        result_valid_friend = self.valid_friend(result_get_friends)
        result_get_friends_groups = self.get_friends_groups(result_valid_friend)
        result_get_unique_groups = self.get_unique_groups(result_get_groups, result_get_friends_groups)
        result_get_group_description = self.get_group_description(result_get_unique_groups)
        self.write_groups_to_json(result_get_group_description)


if __name__ == "__main__":
    spy_games = SpyGames(TOKEN, USER_ID)
    spy_games.get_secret_groups()
