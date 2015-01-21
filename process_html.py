from bs4 import BeautifulSoup

soup = BeautifulSoup(open('faif.html','r'))

for i in soup.find_all('span'):
    if i['class'][0].find('unisong') == 0 or i['class'][0].find('unisong') == 0:
        i.replace_with(i.string)
ccc =soup.prettify()
ccc=ccc.replace('\n     ','')
ccc=ccc.replace('\n    ','')
ccc=ccc.replace('\n   ','')

import codecs
fff=codecs.open('faif-1.0_output.html','w','utf-8')
fff.write(ccc)
fff.close()
# fff=codecs.open('bbb.html','w','utf-8')
# fff.write(soup.prettify())
# fff.close()

# soup = BeautifulSoup(open('aaa.html','r'))
# for i in soup.find_all('p'):
#     if i['class'][0].find('indent') == 0:
#         print str(i)
#         i.string = str(i).replace("\n   ",'')

# import codecs
# fff=codecs.open('bbb.html','w','utf-8')
# fff.write(soup.prettify())
# fff.close()
