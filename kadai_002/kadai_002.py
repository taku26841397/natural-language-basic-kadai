from bs4 import BeautifulSoup
from urllib import request
import re

#本文のスクレイピング
url='https://www.aozora.gr.jp/cards/000148/files/2371_13943.html'

response=request.urlopen(url)
soup=BeautifulSoup(response)
response.close()

main_text=soup.find('div',class_='main_text')

# tags_to_delete=main_text.find_all(['rp','rt'])
# for tag in tags_to_delete:
#     tag.decompose()
main_text=main_text.get_text()


main_text=re.sub(r"[\u3000 \n\r]","",main_text)

print(main_text)



#ストップワードのスクレイピング
url2="http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt"

response=request.urlopen(url2)
soup2=BeautifulSoup(response)
response.close()

stopwords_text=soup2.text
#print(stopwords_text)

stopwords_list=stopwords_text.split("\r\n")
stopwords_list=[word for word in stopwords_list if word]
#print(stopwords_list)

#ストップワードの除去
split_text_list=['近頃','は','大分','方々','の','雑誌','から','談話','を','しろしろ','と','責め','られて','、','頭','が','がらん胴','に','なった','から','、','当分','品','切れ','の','看板','でも','懸け','たい','くらい','に','思って','います','。']
result_text_list=list()
for split_text in split_text_list:
    if split_text not in stopwords_list:
        result_text_list.append(split_text)

print(result_text_list)

