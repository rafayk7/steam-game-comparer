import requests
import json
from collections import Counter

STEAM_API_KEY = '4B49A370474D2FF3930407D3BDEC78B2'

def get_steam_id(STEAM_USERNAME):
	STEAM_ID_URL = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=4B49A370474D2FF3930407D3BDEC78B2&vanityurl=' + str(STEAM_USERNAME)
	steamidjson = requests.get(STEAM_ID_URL)
	steamidedit = json.loads(json.dumps(steamidjson.json()))
	steamid = steamidedit["response"]["steamid"]
	return steamid

def get_games(STEAM_ID):
	global together_ids
	together_ids = []
	STEAM_API_URL = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + str(STEAM_API_KEY) + "&steamid=" + str(STEAM_ID) + "&format=json"
	user_info = requests.get(STEAM_API_URL)
	global json_str
	json_str = json.dumps(user_info.json()) 
	data2 = json.loads(json_str)
	#Adds all of the appids of owned games into the union list
	for i in range(data2["response"]["game_count"]):
		together_ids.append(data2["response"]["games"][i]["appid"])
	return together_ids

def get_same_games(LIST_OF_GAMES):
	global same_games
	cnt = Counter(LIST_OF_GAMES)
	same_games = [k for k, v in cnt.iteritems() if v > 1]
	return same_games

a = "C:/Users/rafayk7/Documents/Steam_game_comparer/allappids.txt"
b = "C:/Users/rafayk7/Documents/Steam_game_comparer/allappnames.txt"


file=open(a)
file2=open(b)

all_appids = list(file)
all_appnames = list(file2)
element_number = []

def get_id_position(LIST):
	for i in range(len(LIST)):
		for j in range(len(all_appids)):
			if LIST[i] == all_appids[j]:
				element_number.append(j)
			else:
				j+=1
	return element_number

def get_game_name(elements):
	global game_names
	game_names = []
	for i in range(len(elements)):
		game_names.append(all_appnames[elements[i]])
	return game_names