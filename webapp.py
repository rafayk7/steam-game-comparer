from flask import Flask, request, render_template, session
import steamapifunctions as p
from collections import Counter
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.secret_key = 'lol'


@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/twopeople')
def twopeople():
	return render_template('twopeople.html')

@app.route('/twopeople', methods=['POST'])
def compare_two():
	#TODO: Use JWT instead of sessions
	if 'visits' in session:
		session['visits'] = session.get('visits') + 1
	else:
		session['visits'] = 1

	names = []
	steamids = []
	
	names.extend([request.form['name1'], request.form['name2']])
	
	try:
		for i in range(len(names)):
			steamids.append(p.get_steam_id(names[i]))
	except KeyError:
		return render_template('errorpage.html')
	
	steamid = [str(item) for item in steamids]
	games_for_first = p.get_games(int(steamid[0]))
	games_for_second = p.get_games(int(steamid[1]))
	games = games_for_first + games_for_second

	cnt = Counter(games)
	same_games_strings = [k for k, v in cnt.iteritems() if v > 1]

	same_games_ints = [str(item) + "\n" for item in same_games_strings]
	elements = p.get_id_position(same_games_ints)

	display = []
	if int(session.get('visits'))>1:
		display = elements[:(len(elements)/(int(session.get('visits'))))]
		return render_template('displayresults.html', game_list=p.get_game_name(display))
	else:
		return render_template('displayresults.html', game_list=p.get_game_name(elements))

@app.route('/threepeople')
def threepeople():
	return render_template('threepeople.html')

@app.route('/threepeople', methods=['POST'])
def compare_three():
	if 'visits' in session:
		session['visits'] = session.get('visits') + 1
	else:
		session['visits'] = 1

	names = []
	steamids = []
	names.extend([request.form['name1'], request.form['name2'], request.form['name3']])
	
	try:
		for i in range(len(names)):
			steamids.append(p.get_steam_id(names[i]))
	except KeyError:
		return render_template('errorpage.html')

	steamid = [str(item) for item in steamids]
	games_for_first = p.get_games(int(steamid[0]))
	games_for_second = p.get_games(int(steamid[1]))
	games_for_third = p.get_games(int(steamid[2]))
	games = games_for_first + games_for_second + games_for_third

	cnt = Counter(games)
	same_games_strings = list(set([x for x in LIST_OF_GAMES if LIST_OF_GAMES.count(x) > 2]))

	same_games_ints = [str(item) + "\n" for item in same_games_strings]
	elements = p.get_id_position(same_games_ints)
	display = []
	
	if int(session.get('visits'))>1:
		display = elements[:(len(elements)/(int(session.get('visits'))))]
		return render_template('displayresults.html', game_list=p.get_game_name(display))
	else:
		return render_template('displayresults.html', game_list=p.get_game_name(elements))

if __name__=="__main__":
    app.run(debug=True)
