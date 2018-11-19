"""Case-study #4 Парсинг web-страниц
Разработчики:
Zikova K.(),Zhambaeva D.()

"""
import urllib.request
#1
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
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_1,att_1,yds_1,td_1,int_1))
#2
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
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_2,att_2,yds_2,td_2,int_2))
#3
url = 'http://www.nfl.com/player/mattmoore/2507282/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_3 = text[text.find(">",one_name)+47:text.find("&",one_name)-1416]
att_3 = text[text.find(">",one_name)+101:text.find("&",one_name)-1362]
fore_3 = text[text.find(">",one_name)+210:text.find("&",one_name)-1251]
celoe = fore_3.find(",")
a = fore_3[:celoe]
b = fore_3[celoe+1:]
yds_3 = (a + b)
td_3 = text[text.find(">",one_name)+320:text.find("&",one_name)-1144]
int_3 = text[text.find(">",one_name)+373:text.find("&",one_name)-1091]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_3,att_3,yds_3,td_3,int_3))
#4
url = 'http://www.nfl.com/player/ajmccarron/2543497/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_4 = text[text.find(">",one_name)+47:text.find("&",one_name)-1376]
att_4 = text[text.find(">",one_name)+100:text.find("&",one_name)-1322]
yds_4 = text[text.find(">",one_name)+209:text.find("&",one_name)-1213]
td_4 = text[text.find(">",one_name)+317:text.find("&",one_name)-1107]
int_4 = text[text.find(">",one_name)+369:text.find("&",one_name)-1055]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_4,att_4,yds_4,td_4,int_4))
#5
url = 'http://www.nfl.com/player/ryanmallett/2495443/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_5 = text[text.find(">",one_name)+47:text.find("&",one_name)-1413]
att_5 = text[text.find(">",one_name)+101:text.find("&",one_name)-1359]
fore_5 = text[text.find(">",one_name)+210:text.find("&",one_name)-1248]
celoe = fore_5.find(",")
a = fore_5[:celoe]
b = fore_5[celoe+1:]
yds_5 = (a + b)
td_5 = text[text.find(">",one_name)+320:text.find("&",one_name)-1142]
int_5 = text[text.find(">",one_name)+372:text.find("&",one_name)-1089]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_5,att_5,yds_5,td_5,int_5))
#6
url = 'http://www.nfl.com/player/landryjones/2539287/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_6 = text[text.find(">",one_name)+47:text.find("&",one_name)-1379]
att_6 = text[text.find(">",one_name)+101:text.find("&",one_name)-1325]
fore_6 = text[text.find(">",one_name)+210:text.find("&",one_name)-1214]
celoe = fore_6.find(",")
a = fore_6[:celoe]
b = fore_6[celoe+1:]
yds_6 = (a + b)
td_6 = text[text.find(">",one_name)+320:text.find("&",one_name)-1108]
int_6 = text[text.find(">",one_name)+372:text.find("&",one_name)-1056]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_6,att_6,yds_6,td_6,int_6))
#7
url = 'http://www.nfl.com/player/robertgriffiniii/2533033/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_7 = text[text.find(">",one_name)+47:text.find("&",one_name)-1391]
at_7 = text[text.find(">",one_name)+101:text.find("&",one_name)-1335]
celoe_1 = at_7.find(",")
e = at_7[:celoe_1]
r = at_7[celoe_1+1:]
att_7 = (e + r)
fore_7 = text[text.find(">",one_name)+212:text.find("&",one_name)-1224]
celoe_2 = fore_7.find(",")
a = fore_7[:celoe_2]
b = fore_7[celoe_2+1:]
yds_7 = (a + b)
td_7 = text[text.find(">",one_name)+322:text.find("&",one_name)-1118]
int_7 = text[text.find(">",one_name)+375:text.find("&",one_name)-1064]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_7,att_7,yds_7,td_7,int_7))
#8
url = 'http://www.nfl.com/player/alextanney/2534870/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_8 = text[text.find(">",one_name)+47:text.find("&",one_name)-1372]
att_8 = text[text.find(">",one_name)+100:text.find("&",one_name)-1319]
yds_8 = text[text.find(">",one_name)+208:text.find("&",one_name)-1211]
td_8 = text[text.find(">",one_name)+315:text.find("&",one_name)-1105]
int_8 = text[text.find(">",one_name)+367:text.find("&",one_name)-1053]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_8,att_8,yds_8,td_8,int_8))
#9
url = 'http://www.nfl.com/player/tomsavage/2543640/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_9 = text[text.find(">",one_name)+47:text.find("&",one_name)-1379]
att_9 = text[text.find(">",one_name)+101:text.find("&",one_name)-1325]
fore_9 = text[text.find(">",one_name)+210:text.find("&",one_name)-1214]
celoe = fore_9.find(",")
a = fore_9[:celoe]
b = fore_9[celoe+1:]
yds_9 = (a + b)
td_9 = text[text.find(">",one_name)+320:text.find("&",one_name)-1108]
int_9 = text[text.find(">",one_name)+372:text.find("&",one_name)-1056]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_9,att_9,yds_9,td_9,int_9))
#10
url = 'http://www.nfl.com/player/scotttolzien/2495425/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_10 = text[text.find(">",one_name)+47:text.find("&",one_name)-1412]
att_10 = text[text.find(">",one_name)+100:text.find("&",one_name)-1358]
fore_10 = text[text.find(">",one_name)+209:text.find("&",one_name)-1247]
celoe = fore_10.find(",")
a = fore_10[:celoe]
b = fore_10[celoe+1:]
yds_10 = (a + b)
td_10 = text[text.find(">",one_name)+319:text.find("&",one_name)-1141]
int_10 = text[text.find(">",one_name)+371:text.find("&",one_name)-1089]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_10,att_10,yds_10,td_10,int_10))
#11
url = 'http://www.nfl.com/player/marksanchez/79858/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
c_11 = text[text.find(">",one_name)+47:text.find("&",one_name)-1426]
celoe_1 = c_11.find(",")
q = c_11[:celoe_1]
w = c_11[celoe_1+1:]
comp_11 = (q + w)
at_11 = text[text.find(">",one_name)+103:text.find("&",one_name)-1370]
celoe_2 = at_11.find(",")
e = at_11[:celoe_2]
r = at_11[celoe_2+1:]
att_11 = (e + r)
fore_11 = text[text.find(">",one_name)+214:text.find("&",one_name)-1258]
celoe_3 = fore_11.find(",")
a = fore_11[:celoe_3]
b = fore_11[celoe_3+1:]
yds_11 = (a + b)
td_11 = text[text.find(">",one_name)+325:text.find("&",one_name)-1151]
int_11 = text[text.find(">",one_name)+378:text.find("&",one_name)-1098]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_11,att_11,yds_11,td_11,int_11))
#12
url = 'http://www.nfl.com/player/kellenclemens/2506895/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_12 = text[text.find(">",one_name)+47:text.find("&",one_name)-1417]
att_12 = text[text.find(">",one_name)+101:text.find("&",one_name)-1363]
fore_12 = text[text.find(">",one_name)+210:text.find("&",one_name)-1252]
celoe = fore_12.find(",")
a = fore_12[:celoe]
b = fore_12[celoe+1:]
yds_12 = (a + b)
td_12 = text[text.find(">",one_name)+320:text.find("&",one_name)-1145]
int_12 = text[text.find(">",one_name)+373:text.find("&",one_name)-1092]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_12,att_12,yds_12,td_12,int_12))
#13
url = 'http://www.nfl.com/player/ryannassib/2539961/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_13 = text[text.find(">",one_name)+47:text.find("&",one_name)-1410]
att_13 = text[text.find(">",one_name)+99:text.find("&",one_name)-1357]
yds_13 = text[text.find(">",one_name)+207:text.find("&",one_name)-1248]
td_13 = text[text.find(">",one_name)+316:text.find("&",one_name)-1141]
int_13 = text[text.find(">",one_name)+368:text.find("&",one_name)-1089]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_13,att_13,yds_13,td_13,int_13))
#14
url = 'http://www.nfl.com/player/danorlovsky/2506481/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_14 = text[text.find(">",one_name)+47:text.find("&",one_name)-1416]
att_14 = text[text.find(">",one_name)+101:text.find("&",one_name)-1362]
fore_14 = text[text.find(">",one_name)+210:text.find("&",one_name)-1251]
celoe = fore_14.find(",")
a = fore_14[:celoe]
b = fore_14[celoe+1:]
yds_14 = (a + b)
td_14 = text[text.find(">",one_name)+320:text.find("&",one_name)-1144]
int_14 = text[text.find(">",one_name)+373:text.find("&",one_name)-1091]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_14,att_14,yds_14,td_14,int_14))
#15
url = 'http://www.nfl.com/player/teddybridgewater/2543465/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_15 = text[text.find(">",one_name)+47:text.find("&",one_name)-1384]
att_15 = text[text.find(">",one_name)+101:text.find("&",one_name)-1330]
fore_15 = text[text.find(">",one_name)+210:text.find("&",one_name)-1219]
celoe = fore_15.find(",")
a = fore_15[:celoe]
b = fore_15[celoe+1:]
yds_15 = (a + b)
td_15 = text[text.find(">",one_name)+320:text.find("&",one_name)-1112]
int_15 = text[text.find(">",one_name)+373:text.find("&",one_name)-1059]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_15,att_15,yds_15,td_15,int_15))
#16
url = 'http://www.nfl.com/player/brianhoyer/81294/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_16 = text[text.find(">",one_name)+47:text.find("&",one_name)-1385]
at_16 = text[text.find(">",one_name)+101:text.find("&",one_name)-1329]
celoe = at_16.find(",")
q = at_16[:celoe]
w = at_16[celoe+1:]
att_16 = (q + w)
fore_16 = text[text.find(">",one_name)+212:text.find("&",one_name)-1218]
celoe_2 = fore_16.find(",")
a = fore_16[:celoe_2]
b = fore_16[celoe_2+1:]
yds_16 = (a + b)
td_16 = text[text.find(">",one_name)+322:text.find("&",one_name)-1111]
int_16 = text[text.find(">",one_name)+375:text.find("&",one_name)-1058]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_16,att_16,yds_16,td_16,int_16))
#17
url = 'http://www.nfl.com/player/mattschaub/2505982/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
c_17 = text[text.find(">",one_name)+47:text.find("&",one_name)-1392]
celoe_1 = c_17.find(",")
q = c_17[:celoe_1]
w = c_17[celoe_1+1:]
comp_17 = (q + w)
at_17 = text[text.find(">",one_name)+103:text.find("&",one_name)-1336]
celoe_2 = at_17.find(",")
e = at_17[:celoe_2]
r = at_17[celoe_2+1:]
att_17 = (e + r)
fore_17 = text[text.find(">",one_name)+214:text.find("&",one_name)-1224]
celoe_3 = fore_17.find(",")
a = fore_17[:celoe_3]
b = fore_17[celoe_3+1:]
yds_17 = (a + b)
td_17 = text[text.find(">",one_name)+325:text.find("&",one_name)-1116]
int_17 = text[text.find(">",one_name)+379:text.find("&",one_name)-1063]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_17,att_17,yds_17,td_17,int_17))
#18
url = 'http://www.nfl.com/player/derekanderson/2506546/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_18 = text[text.find(">",one_name)+47:text.find("&",one_name)-1388]
at_18 = text[text.find(">",one_name)+101:text.find("&",one_name)-1332]
celoe_2 = at_18.find(",")
e = at_18[:celoe_2]
r = at_18[celoe_2+1:]
att_18 = (e + r)
fore_18 = text[text.find(">",one_name)+212:text.find("&",one_name)-1220]
celoe_3 = fore_18.find(",")
a = fore_18[:celoe_3]
b = fore_18[celoe_3+1:]
yds_18 = (a + b)
td_18 = text[text.find(">",one_name)+323:text.find("&",one_name)-1113]
int_18 = text[text.find(">",one_name)+376:text.find("&",one_name)-1060]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_18,att_18,yds_18,td_18,int_18))
#19
url = 'http://www.nfl.com/player/lukemccown/2506053/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_19 = text[text.find(">",one_name)+47:text.find("&",one_name)-1415]
att_19 = text[text.find(">",one_name)+101:text.find("&",one_name)-1361]
fore_19 = text[text.find(">",one_name)+210:text.find("&",one_name)-1250]
celoe = fore_19.find(",")
a = fore_19[:celoe]
b = fore_19[celoe+1:]
yds_19 = (a + b)
td_19 = text[text.find(">",one_name)+320:text.find("&",one_name)-1144]
int_19 = text[text.find(">",one_name)+372:text.find("&",one_name)-1091]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_19,att_19,yds_19,td_19,int_19))
#20
url = 'http://www.nfl.com/player/mattbarkley/2539308/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_20 = text[text.find(">",one_name)+47:text.find("&",one_name)-1381]
att_20 = text[text.find(">",one_name)+101:text.find("&",one_name)-1327]
fore_20 = text[text.find(">",one_name)+210:text.find("&",one_name)-1216]
celoe = fore_20.find(",")
a = fore_20[:celoe]
b = fore_20[celoe+1:]
yds_20 = (a + b)
td_20 = text[text.find(">",one_name)+320:text.find("&",one_name)-1109]
int_20 = text[text.find(">",one_name)+373:text.find("&",one_name)-1056]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_20,att_20,yds_20,td_20,int_20))
#21
url = 'http://www.nfl.com/player/thadlewis/497121/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_21 = text[text.find(">",one_name)+47:text.find("&",one_name)-1413]
att_21 = text[text.find(">",one_name)+101:text.find("&",one_name)-1359]
fore_21 = text[text.find(">",one_name)+210:text.find("&",one_name)-1248]
celoe = fore_21.find(",")
a = fore_21[:celoe]
b = fore_21[celoe+1:]
yds_21 = (a + b)
td_21 = text[text.find(">",one_name)+320:text.find("&",one_name)-1142]
int_21 = text[text.find(">",one_name)+372:text.find("&",one_name)-1090]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_21,att_21,yds_21,td_21,int_21))
#22
url = 'http://www.nfl.com/player/seanmannion/2552576/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]

one_name = text.find("TOTAL")
comp_22 = text[text.find(">",one_name)+47:text.find("&",one_name)-1375]
att_22 = text[text.find(">",one_name)+100:text.find("&",one_name)-1322]
yds_22 = text[text.find(">",one_name)+208:text.find("&",one_name)-1213]
td_22 = text[text.find(">",one_name)+316:text.find("&",one_name)-1107]
int_22 = text[text.find(">",one_name)+368:text.find("&",one_name)-1055]
print('{:20} {:7} {:7} {:7} {:7} {:7}'.format(name,comp_22,att_22,yds_22,td_22,int_22))





