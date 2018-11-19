"""Case-study #4 Парсинг web-страниц
Разработчики:
Zikova K.(),Zhambaeva D.()

"""
import urllib.request
#first player
url = 'http://www.nfl.com/player/brycepetty/2552369/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_1 = text[text.find(">",one_name)+47:text.find("&",one_name)-1380]
att_1 = text[text.find(">",one_name)+101:text.find("&",one_name)-1326]
fore_1 = text[text.find(">",one_name)+210:text.find("&",one_name)-1215]
celoe = fore_1.find(",")
a = fore_1[:celoe]
b = fore_1[celoe+1:]
yds_1 = (a + b)
td_1 = text[text.find(">",one_name)+320:text.find("&",one_name)-1109]
int_1 = text[text.find(">",one_name)+372:text.find("&",one_name)-1056]
print('{:15} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_1,att_1,yds_1,td_1,int_1))

#second player
url = 'http://www.nfl.com/player/jimmygaroppolo/2543801/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_2 = text[text.find(">",one_name)+47:text.find("&",one_name)-1380]
att_2 = text[text.find(">",one_name)+101:text.find("&",one_name)-1326]
fore_2 = text[text.find(">",one_name)+210:text.find("&",one_name)-1215]
celoe = fore_2.find(",")
a = fore_2[:celoe]
b = fore_2[celoe+1:]
yds_2 = (a + b)
td_2 = text[text.find(">",one_name)+320:text.find("&",one_name)-1109]
int_2 = text[text.find(">",one_name)+373:text.find("&",one_name)-1056]
print('{:15} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_2,att_2,yds_2,td_2,int_2))








