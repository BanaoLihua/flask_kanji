import requests
from bs4 import BeautifulSoup
import re
import csv

# 部首のURLを指定して漢字と読みを取得
url = 'https://kanji.jitenon.jp/cat/bushu04004.html'

# CSVファイル
path = '/Users/hobby/Desktop/study/kanji_ki.csv'

with open(path, 'w', encoding="utf_8") as f:
    writer = csv.writer(f)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    kanji_lst = soup.select(".search_parts li > a")
    for str in kanji_lst:
        output_list = []
        kanji = str.get_text()
        output_list.append(kanji)
        kanji_url = str.get('href')
        r2 = requests.get(kanji_url)
        soup2 = BeautifulSoup(r2.content, "html.parser")
        yomi_lst = soup2.select(
            "#content > div.search_data > div > div.word_box > ul > li > h3 > span.yomi, #content > div.search_data > div > div.word_box > ul > li > a > h3 > span.yomi")
        formatted_yomi_lst = []
        for str2 in yomi_lst:
            text = re.sub("\（|\）", "", str2.get_text())
            formatted_yomi_lst.append(text)
        yomi = '、'.join(formatted_yomi_lst)
        output_list.append(yomi)
        # 読みが無い時飛ばす
        if output_list[1] == "":
            continue
        writer.writerow(output_list)