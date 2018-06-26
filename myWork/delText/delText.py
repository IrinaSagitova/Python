import chardet
import re

TEXT_FILE = 'taro.txt'

class DelText:

    def __init__(self, text_file):
        self.text_file = TEXT_FILE

    def get_delete(self):
        with open(self.text_file, 'rb') as file:
            file_read = file.read()
            result = chardet.detect(file_read)
            f = file_read.decode(result['encoding'])
        print(re.sub(r'\(.*?\)', '', f))

if __name__ == "__main__":
    del_text = DelText(TEXT_FILE)
    del_text.get_delete()