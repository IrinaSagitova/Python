import requests
from bs4 import BeautifulSoup
import re
import csv

WEB_PAGE = requests.get('https://elibrary.ru/item.asp?id=24357001')
FILENAME = 'test.csv'

class Parsing:

  def __init__(self, web_page, filename):
    self.web_page = WEB_PAGE
    self.filename = FILENAME

  def get_title(self):
    soup = BeautifulSoup(self.web_page.text, 'html.parser')
    title = soup.find('title')
    title = str(title)
    title = title[title.find('>') + 1:]
    title = title.rsplit('<', 1)
    title = title[0]
    result_title = title.strip()
    return result_title

  def get_magazine_title(self):
    soup = BeautifulSoup(self.web_page.text, 'html.parser')
    magazine_title = soup.find('a', title="Оглавления выпусков этого журнала")
    mt = str(magazine_title)
    mt = mt[mt.find('>') + 1:]
    mt = mt.rsplit('<', 1)
    mt = mt[0]
    result_mt = mt.strip()
    return result_mt

  def get_publ_num(self):
    soup = BeautifulSoup(self.web_page.text, 'html.parser')
    publ_num = soup.find_all('a', title="Оглавление выпуска")
    pn = str(publ_num)
    pn = pn[pn.find('>') + 1:]
    pn = pn.rsplit('<', 1)
    pn = pn[0]
    result_pn = pn.strip()
    return result_pn

  def get_publ(self):
    soup = BeautifulSoup(self.web_page.text, 'html.parser')
    publ = soup.find('a', title="Список журналов этого издательства")
    publ = str(publ)
    publ = publ[publ.find('>') + 1:]
    publ = publ.rsplit('<', 1)
    publ = publ[0]
    result_publ = publ.strip()
    return result_publ

  def get_year_publ(self):
    soup = BeautifulSoup(self.web_page.text, 'html.parser')
    regexp = r'\d{4}$'
    year_publ = soup.find('font', text=re.compile(regexp))
    yp = str(year_publ)
    yp = yp[yp.find('>') + 1:]
    yp = yp.rsplit('<', 1)
    yp = yp[0]
    result_yp = yp.strip()
    return result_yp

  def get_write_to_csv(self):
    data = self.get_title(), self.get_magazine_title(), self.get_publ_num(), self.get_publ(), self.get_year_publ()
    with open(self.filename, 'w', newline='', encoding='utf-8') as file:
      csv.writer(file).writerow(data)

if __name__ == "__main__":
  parsing = Parsing(WEB_PAGE, FILENAME)
  parsing.get_write_to_csv()