
# coding: utf-8

# In[1]:


import requests
import chardet
import os


# In[2]:


key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'


# In[3]:


def find_lang(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
    params = {
        'key': key,
        'text': text
    }
    response = requests.get(url, params=params).json()
    return response['lang']


# In[4]:


def translate_it(text, *args):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'key': key,
        'lang': '-'.join(args),
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


# In[5]:


def get_lang():
    url = 'https://translate.yandex.net/api/v1.5/tr.json/getLangs'
    params = {
        'key': key,
        'an': 'ru'
    }
    response = requests.get(url, params=params).json()
    return response.get('langs', [])


# In[6]:


def keep_text(text, file):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)


# In[7]:


def load_text(file):
    with open(file, 'rb') as f:
        ab = f.read()
        enc = chardet.detect(ab)
        return ab.decode(enc['encoding'])


# In[8]:


OBJECT_LANG = 'ru'
PRODUCT = os.path.join(os.curdir, OBJECT_LANG)


# In[9]:


if not os.path.exists(PRODUCT):
    os.makedirs(PRODUCT)


# In[17]:


for origin_file in os.listdir(os.curdir):
    if origin_file.endswith('.txt'):
        object_file = os.path.join(PRODUCT, '.'.join([OBJECT_LANG, origin_file]))
        origin_file = os.path.join(os.curdir, origin_file)
        print('\Translate "{}"'.format(origin_file))
        src_text = load_text(origin_file)
        translation = translate_it(src_text, OBJECT_LANG)
        keep_text(translation, object_file)
        print('saved  to "{}".'.format(object_file))

