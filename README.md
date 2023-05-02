# smartbase_server
 A python https server for company "SmartBase".
 This server works like a proxy-server, and made specially for SmartBase API. 
 For working http server you must run app.py. Server has 2 methods - post and get, post - refresh data, get - sending back data.
 databaseSetup.py is for setting up server dataBase for cache data, that we get from other API.
 cacheData.py request from SmartBase API data.
 Python version - 3.10.11.
 All packages - requirements.txt.
 For migrations here used peewee-migrations library, to make migration go to directory of this project in shell,
 then add models to watchlist using this command - "pem add here_file_and_model_name", example "pem add databaseModel.Data".
 For migrations - 'pem migrate'.
 For available migrations - 'pem list'
 Response example - response.json