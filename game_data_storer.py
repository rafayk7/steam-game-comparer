import simplejson
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

a = "C:/Users/rafayk7/Documents/Steam_game_comparer/allgamedata.txt"

with open(a) as data:
    content = simplejson.load(data)

all_appids = []
total_games = len(content["applist"]["apps"])

for i in range(total_games):
    appid = content["applist"]["apps"][i]["appid"]
    all_appids.append(appid)

all_appnames = []
for i in range(total_games):
    appname = content["applist"]["apps"][i]["name"]
    all_appnames.append(appname)

file_to_save2 = open("allappnames.txt", 'w')

for item in all_appnames:
	file_to_save2.write("%s\n" % item)

file_to_save = open("allappids.txt", 'w')

for item in all_appids:
    file_to_save.write("%s\n" % item)

