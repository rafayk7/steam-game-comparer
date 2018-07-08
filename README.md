# steam-game-comparer

This is a website that makes Steam API calls to check which games any two or three users have in common. 
# webapp.py

This is the main Flask application used for POST and GET requests from the webpage, and to perform functions stored in steamapifunctions.py

# steamapifunctions.py

This is the file storing all of the functions needed to perform the steam API calls, such as to get the steamid from the username, getting the games from the username, and non-steam API functions as well such as to see which games they share, and to convert it from the appid to its name. 

# game_data_storer.py

This is the file used to create the allappids.txt and allappnames.txt files. These are the files that store the name and appid for each steam app, allowing the conversion of appid to name. 

# allappids.txt, allappnames.txt, allgamenames.json

These are the files that contain the data for all apps on the Steam database. There is an alternative version that scrapes steamdb.com, but this version is much slower as it scrapes the website individually for each game. That is why a cache was created, to improve efficiency and reduce time taken for the app to run. 

To test the app, the following steam usernames can be used: rafayk7 and vimalrj. 
