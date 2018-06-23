import chardet
import json

def get_encoding(file):
    return chardet.detect(open(file, 'rb').read())['encoding']

def get_file(file):
    print('file is {}'.format(file))
    enc = get_encoding(file)
    return open(file, 'r', encoding=enc)

def get_words(var):
    counter = {}
    for s in var:
        for word in s.strip().lower().split(' '):
            if len(word) > 6:
                count = counter.get(word, 0)
                counter[word] = count + 1
    return counter

def get_list(adict):
    rank_list = list(zip(adict.values(), adict.keys()))
    rank_list.sort(reverse=True)
    return rank_list
    
def get_json(ivar):
    result = []
    if type(ivar) is dict:
        for key in ivar.keys():
            result += get_json(ivar[key])
    elif type(ivar) is list:
        for itm in ivar:
            result += get_json(itm)
    else:
        result.append(ivar)
    return result    

def print_rank(ranked):
    for i in range(10):
        print(ranked[i])

def parse_rank_and_print(raw_list):
    print_rank(
        get_list(
            get_words(raw_list)
        )
    )

def act(file):
    if file.endswith('.json'):
      parse_rank_and_print(get_json(json.load(get_file(file))))

def act_all():
    act('newsafr.json')
    act('newscy.json')
    act('newsfr.json')
    act('newsit.json')

def push():
    file = input('input filename: ')
    if not file:
        act_all()
    else:
        act(file)

push()